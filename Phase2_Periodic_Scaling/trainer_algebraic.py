import torch
import torch.nn as nn
import torch.optim as optim
import os
import json

def load_data():
    dataset_path = os.path.join(os.path.dirname(__file__), 'covalent_dataset.json')
    with open(dataset_path, 'r') as f:
        return json.load(f)
def dict_to_tensor(atom_dict):
    return torch.tensor([[atom_dict['Z'], atom_dict['N'], atom_dict['n'], atom_dict['v']]], dtype=torch.float32)

from model_bonding import CouplingWhitebox
from model_algebraic import AlgebraicNode

def build_algebraic_engine():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = CouplingWhitebox()
    # We sever the AI/Deep Learning layer entirely.
    # We insert the 9-parameter fundamental foundational physics algebra.
    model.atomic_node = AlgebraicNode()
    model = model.to(device)
    return model, device

def train_algebraic_engine():
    print("Loading fundamental geometrical atomic datasets...")
    dataset = load_data()
    train_data = dataset['training']
    test_data = dataset['testing']
    
    model, device = build_algebraic_engine()
    
    save_path = os.path.join(os.path.dirname(__file__), 'twt_algebraic_engine.pth')
    if os.path.exists(save_path):
        print(f"[SYSTEM] Existing algebraic constants found! Loading checkpoint from {save_path} ...")
        model.load_state_dict(torch.load(save_path, map_location=device))
        print("Model loaded successfully. Continuing deep algebraic optimization.\n")
    else:
        print("[SYSTEM] No previous checkpoint found. Starting algebraic derivation from scratch.\n")
        
    optimizer = optim.Adam(model.parameters(), lr=0.01) 
    criterion = nn.MSELoss()
    
    epochs = 400
    
    print("===================================================================")
    print(" Booting TWT Pure Algebraic Continuity Solver (4D True CUDA Grid)")
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
            
            acc = 100 * (1 - abs(pred - target) / target)
            name_A = [k for k, v in [("H",1), ("F",9), ("Cl",17), ("Br",35), ("I",53)] if v == item['atom_A']['Z']][0]
            name_B = [k for k, v in [("H",1), ("F",9), ("Cl",17), ("Br",35), ("I",53)] if v == item['atom_B']['Z']][0]
            molecule_name = f"{name_A}-{name_B}"
            print(f"[UNSEEN] {molecule_name} -> Predicted: {pred:.3f} | Actual: {target:.3f} | Accuracy: {acc:.1f}%")
            
    print("")
    model.atomic_node.extract_algebraic_law()
    print(f"\nThe True Universal Elasticity Modulus of Cl(4,0) discovered by the formulation is Alpha = {model.vacuum_alpha.item():.4f}")
    
    torch.save(model.state_dict(), save_path)
    print(f"\n[SYSTEM] Algebraic Engine frozen and exported to {save_path}.")

if __name__ == '__main__':
    train_algebraic_engine()
