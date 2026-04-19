import torch
import numpy as np
import os
from model_bonding import CouplingWhitebox

def distill_and_extract():
    # Load the pure framework
    model = CouplingWhitebox()
    
    save_path = os.path.join(os.path.dirname(__file__), 'twt_optimized_engine.pth')
    if not os.path.exists(save_path):
        print("Model not found. Please run trainer.py first.")
        return
        
    model.load_state_dict(torch.load(save_path))
    model.eval()
    
    # Extract weights
    W1 = model.atomic_node.cyclic_layer.weight.data.numpy()
    b1 = model.atomic_node.cyclic_layer.bias.data.numpy()
    W2 = model.atomic_node.collapse_layer.weight.data.numpy()
    b2 = model.atomic_node.collapse_layer.bias.data.numpy()
    alpha = model.vacuum_alpha.item()
    
    print("\n========================================================")
    print(" DISTILLING TWT EQUATION STATE")
    print("========================================================\n")
    
    # Distillation pass (Post-hoc pruning instead of aggressive L1 training)
    # Any weight that contributes an absolute scalar modification less than 0.05 is forced to 0
    # to yield a heavily structured, humanly readable law.
    THRESHOLD = 0.05
    W1[np.abs(W1) < THRESHOLD] = 0.0
    b1[np.abs(b1) < THRESHOLD] = 0.0
    W2[np.abs(W2) < THRESHOLD] = 0.0
    b2[np.abs(b2) < THRESHOLD] = 0.0
    
    input_vars = ["Z", "N", "n", "v"]
    
    # We reconstruct the equation algebraically
    print(f"Universal Vacuum Elasticity Modulus (Alpha) = {alpha:.4f}\n")
    
    # There are 8 harmonic cycles (hidden nodes). We write them out if they survived pruning.
    harmonics = []
    for i in range(8):
        terms = []
        for j in range(4):
            if W1[i, j] != 0:
                terms.append(f"({W1[i, j]:.2f} * {input_vars[j]})")
        
        if len(terms) == 0 and b1[i] == 0:
            harmonics.append("0")
        else:
            inner = " + ".join(terms)
            if b1[i] != 0:
                inner += f" + {b1[i]:.2f}"
            harmonics.append(f"sin({inner})")
            
    # Map bounds (S=0, P=1, D=2)
    labels = ["S (Continuous Expansion)", "P (Chiral Polarity)", "D (Core Resistance)"]
    
    for k in range(3):
        print(f"[{labels[k]}] Equation:")
        terms = []
        for h in range(8):
            if W2[k, h] != 0 and harmonics[h] != "0":
                terms.append(f"({W2[k, h]:.2f} * H_{h+1})")
                
        if len(terms) == 0:
            equation = f"| {b2[k]:.2f} | + 0.5"
        else:
            equation = f"| " + " + ".join(terms)
            if b2[k] != 0:
                equation += f" + {b2[k]:.2f}"
            equation += f" | + 0.5"
            
        print("  " + equation)
        
        # Display the active harmonics mapping
        for h in range(8):
            if W2[k, h] != 0 and harmonics[h] != "0":
                print(f"    * H_{h+1} = {harmonics[h]}")
        print("")
        
if __name__ == '__main__':
    distill_and_extract()
