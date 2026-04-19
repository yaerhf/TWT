"""
TWT: The Atomic Whitebox Model (Phase 2)
===================================================================
A fully interpretable geometric neural matrix. 
Unlike standard Deep Learning Blackboxes containing millions of weights, 
this architecture is strictly bottlenecked to enforce equation distillation.

INPUT: [Z (Protons), N (Neutrons), n (Shell Index), v (Valence Electrons)]
OUTPUT: [S (Topological Extent), P (Chiral Polarity), D (Core Density)]

By forcing the network to solve organic chemistry through only 8 cyclic 
parameters, the optimized weights will represent a direct mathematical 
equation describing how nucleons compress continuous space.
"""

import torch
import torch.nn as nn

class AtomicWhitebox(nn.Module):
    def __init__(self):
        super(AtomicWhitebox, self).__init__()
        
        # Layer 1: The Cyclic Transformer 
        # We project 4 discrete quantum integers into 8 continuous harmonic spaces.
        self.cyclic_layer = nn.Linear(in_features=4, out_features=8, bias=True)
        
        # Layer 2: The Topological Collapse
        # We collapse the 8 harmonic states directly into the 3 TWT boundaries.
        self.collapse_layer = nn.Linear(in_features=8, out_features=3, bias=True)

    def forward(self, x):
        """
        x is a tensor input: [Z, N, n, v]
        """
        # We apply torch.sin() as the activation. 
        # This literally forces the network to calculate physical 'periodicity' 
        # instead of abstract linear scaling. It invents Phase / Quantum Shells.
        harmonic_state = torch.sin(self.cyclic_layer(x))
        
        # Collapse into bounded limits (S, P, D)
        # We use absolute value to enforce strictly positive geometric radii and bounds
        # The +0.5 prevents division-by-zero singularities and ensures the initial random 
        # parameters actually span wide enough to touch across the Cartesian meshgrid!
        twt_bounds = torch.abs(self.collapse_layer(harmonic_state)) + 0.5
        
        # S: Bounds topological expansion (inverse to Z_eff scalar)
        # P: Bounds rotational tension (Electronegativity draw)
        # D: Bounds mass limit at r=0
        
        # We split the tensor for absolute explicit physics mapping
        S = twt_bounds[:, 0]
        P = twt_bounds[:, 1]
        D = twt_bounds[:, 2]
        
        return S, P, D

    def extract_governing_equation(self):
        """
        Once trained, this function prints the literal mathematical formula 
        derived by the AI mapping nucleons directly to continuous elasticity.
        """
        W1 = self.cyclic_layer.weight.data.cpu().numpy()
        b1 = self.cyclic_layer.bias.data.cpu().numpy()
        W2 = self.collapse_layer.weight.data.cpu().numpy()
        b2 = self.collapse_layer.bias.data.cpu().numpy()
        
        print("\n--- DERIVED ATOMIC TWT EQUATION ---")
        print("S (Extent)   = | Sum( W2_0 * sin(W1*X + b1) ) + b2_0 | + 0.01")
        print("P (Polarity) = | Sum( W2_1 * sin(W1*X + b1) ) + b2_1 | + 0.01")
        print("D (Density)  = | Sum( W2_2 * sin(W1*X + b1) ) + b2_2 | + 0.01")
        print("\nRaw Tensor Matrices ready for distillation scaling.")
        return W1, b1, W2, b2

if __name__ == '__main__':
    # Initial untrained test
    model = AtomicWhitebox()
    sample_fluorine = torch.tensor([[9.0, 10.0, 2.0, 7.0]]) # F: Z=9, N=10, n=2, v=7
    S, P, D = model(sample_fluorine)
    print(f"Untrained Abstract Output for Fluorine: S={S.item():.4f}, P={P.item():.4f}, D={D.item():.4f}")
