import json
import torch
import torch.nn as nn
import torch.optim as optim
import os
from model_bonding import CouplingWhitebox

def load_data():
    path = os.path.join(os.path.dirname(__file__), 'covalent_dataset.json')
    with open(path, 'r') as f:
        return json.load(f)

def dict_to_tensor(d):
    # [Z, N, n, v]
    return torch.tensor([[d['Z'], d['N'], d['n'], d['v']]], dtype=torch.float32)

def train_twt_engine():
    dataset = load_data()
    train_data = dataset['training']
    test_data = dataset['testing']
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = CouplingWhitebox().to(device)
    
    save_path = os.path.join(os.path.dirname(__file__), 'twt_optimized_engine.pth')
    if os.path.exists(save_path):
        print(f"[SYSTEM] Existing optimized engine found! Loading checkpoint from {save_path} ...")
        model.load_state_dict(torch.load(save_path, map_location=device))
        print("Model loaded successfully. Continuing deep optimization.\n")
    else:
        print("[SYSTEM] No previous checkpoint found. Starting optimization from scratch.\n")
        
    optimizer = optim.Adam(model.parameters(), lr=0.01) 
    criterion = nn.MSELoss()
    
    epochs = 600
    
    print("===================================================================")
    print(" Booting TWT Neural Symbolic Regression Engine (4D True CUDA Grid)")
    print("===================================================================")
    print(f"Training on {len(train_data)} molecules. Validating on {len(test_data)} strictly unseen molecules.\n")
    
    import time
    start_time = time.time()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for item in train_data:
            atom_A = dict_to_tensor(item['atom_A']).to(device)
            atom_B = dict_to_tensor(item['atom_B']).to(device)
            target = torch.tensor([[item['empirical_3D_length']]], dtype=torch.float32, device=device)
            
            optimizer.zero_grad()
            
            prediction = model(atom_A, atom_B)
            
            loss = criterion(prediction, target[0, 0])
            
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
        print(f"Epoch {epoch:03d} | Total Optimization Loss: {total_loss:.4f} | Vacuum Alpha = {model.vacuum_alpha.item():.4f}")
            
    end_time = time.time()
    print(f"\n[TIMING] {epochs} epochs took {end_time - start_time:.2f} seconds.")
    print(f"[ESTIMATION] 400 epochs will take approx {(end_time - start_time) / epochs * 400 / 60:.2f} minutes.")
            
    # Evaluation Phase
    print("\n===================================================================")
    print(" BLIND PREDICTIVE VALIDATION (Evaluating Holdout Molecules)")
    print("===================================================================")
    model.eval()
    with torch.no_grad():
        for item in test_data:
            atom_A = dict_to_tensor(item['atom_A']).to(device)
            atom_B = dict_to_tensor(item['atom_B']).to(device)
            target = item['empirical_3D_length']
            
            pred = model(atom_A, atom_B).item()
            accuracy = (1.0 - abs(pred - target)/target) * 100.0
            
            # Print molecule name for clarity (deriving name from proton count)
            name_A = [k for k, v in [("H",1), ("F",9), ("Cl",17), ("Br",35), ("I",53)] if v == item['atom_A']['Z']][0]
            name_B = [k for k, v in [("H",1), ("F",9), ("Cl",17), ("Br",35), ("I",53)] if v == item['atom_B']['Z']][0]
            
            mol = f"{name_A}-{name_B}"
            print(f"[UNSEEN] {mol.ljust(5)} -> Predicted: {pred:.3f} | Actual: {target:.3f} | Accuracy: {accuracy:.1f}%")
            
    # Extract the Governing Equation
    model.atomic_node.extract_governing_equation()
    print(f"\nThe True Universal Elasticity Modulus of Cl(4,0) discovered by the network is Alpha = {model.vacuum_alpha.item():.4f}")
    
    # Save the Neural Object state for math extraction
    save_path = os.path.join(os.path.dirname(__file__), 'twt_optimized_engine.pth')
    torch.save(model.state_dict(), save_path)
    print(f"\n[SYSTEM] Neural Engine frozen and exported to {save_path} for distillation.")

if __name__ == '__main__':
    train_twt_engine()
