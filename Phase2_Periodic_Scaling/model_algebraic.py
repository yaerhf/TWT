import torch
import torch.nn as nn

class AlgebraicNode(nn.Module):
    """
    Algebraic Extractor Node.
    This replaces the 56-parameter Artificial Neural Network with a 9-parameter foundational continuous geometry algorithm.
    We assert that S, P, and D are not arbitrary step-functions, but explicit topological bounding constraints
    that obey standard multidimensional sphere packing constraints driven intimately by particle vectors.
    """
    def __init__(self):
        super().__init__()
        # S (Continuous Expansion) parameters
        # S directly scales with Topological Volume boundaries. 
        # Standard physics dictates bounds map to Principal Quantum limits vs Nuclear Density mapping
        self.s_scale = nn.Parameter(torch.tensor([1.0]))
        self.s_shift = nn.Parameter(torch.tensor([1.0]))
        self.s_bias  = nn.Parameter(torch.tensor([0.5]))
        self.s_shield = nn.Parameter(torch.tensor([0.5])) # Core electron topological shielding
        
        # P (Chiral Polarity) parameters
        # Polarity represents structural vector alignment or "drag tension" during wave mapping
        self.p_scale = nn.Parameter(torch.tensor([1.0]))
        self.p_shift = nn.Parameter(torch.tensor([1.0]))
        self.p_bias  = nn.Parameter(torch.tensor([0.5]))
        
        # D (Core Density / Resistance) parameters
        # Density peaks linearly with absolute core mass but decays dimensionally with geometric shell expansion.
        self.d_scale = nn.Parameter(torch.tensor([1.0]))
        self.d_shift = nn.Parameter(torch.tensor([1.0]))
        self.d_bias  = nn.Parameter(torch.tensor([0.5]))
        self.d_shield = nn.Parameter(torch.tensor([0.5])) # Nucleon geometric shielding

    def forward(self, atom_params):
        Z = atom_params[:, 0]
        N = atom_params[:, 1]
        n = atom_params[:, 2]
        v = atom_params[:, 3]
        
        # Core inner electron count
        core_electrons = Z - v
        
        # S (Extent) - Topological Radius
        # Bounded by Shell mapping (n^2) crushed inward geometrically by shielded Nuclear Charge 
        Z_eff_s = Z - torch.abs(self.s_shield) * core_electrons
        Z_eff_s = torch.clamp(Z_eff_s, min=0.1) # Prevent mathematical singularity
        S = torch.abs(self.s_scale) * (n**2) / (Z_eff_s + torch.abs(self.s_shift)) + torch.abs(self.s_bias)
        
        # P (Polarity) - MultiVector Tension
        # Reaches density maximums corresponding to heavy Valence saturation mapped against geometric boundaries
        P = torch.abs(self.p_scale) * (v) / (n + torch.abs(self.p_shift)) + torch.abs(self.p_bias)
        
        # D (Density) - Topological Resistance against overlap
        # Linear correlation to shielded absolute nucleus mass drastically dispersed across expanded shell volume (~n^3)
        Z_eff_d = Z - torch.abs(self.d_shield) * core_electrons
        Z_eff_d = torch.clamp(Z_eff_d, min=0.1)
        D = torch.abs(self.d_scale) * (Z_eff_d + N) / (n**3 + torch.abs(self.d_shift)) + torch.abs(self.d_bias)
        
        return S, P, D
        
    def extract_algebraic_law(self):
        print("\n--- DISTILLED FUNDAMENTAL ALGEBRAIC TWT CONSTANTS ---")
        print(f"S (Extent)   = ({torch.abs(self.s_scale).item():.4f} * n^2) / (Z_eff + {torch.abs(self.s_shift).item():.4f}) + {torch.abs(self.s_bias).item():.4f}")
        print(f"P (Polarity) = ({torch.abs(self.p_scale).item():.4f} * v) / (n + {torch.abs(self.p_shift).item():.4f}) + {torch.abs(self.p_bias).item():.4f}")
        print(f"D (Density)  = ({torch.abs(self.d_scale).item():.4f} * (Z_eff+N)) / (n^3 + {torch.abs(self.d_shift).item():.4f}) + {torch.abs(self.d_bias).item():.4f}")
        print(f"S Shield Mod = {torch.abs(self.s_shield).item():.4f}")
        print(f"D Shield Mod = {torch.abs(self.d_shield).item():.4f}")
