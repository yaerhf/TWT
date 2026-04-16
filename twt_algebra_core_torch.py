import torch
import numpy as np
from clifford.g4 import layout

# Attempt to configure CUDA if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"TWT Torch Engine Initializing on: {device}")

class Cl4Engine:
    def __init__(self):
        self.device = device
        self._build_tables()
        
    def _build_tables(self):
        """
        Dynamically construct the 16x16x16 Geometric Product Tensor
        and the 16-element Reversal Signs array directly from the academic library
        to guarantee absolute mathematical fidelity.
        """
        bases = layout.blades_list
        mult_table = np.zeros((16, 16, 16), dtype=np.float32)
        
        for i, bi in enumerate(bases):
            for j, bj in enumerate(bases):
                res = bi * bj
                for k in range(16):
                    mult_table[i, j, k] = res.value[k]
                    
        self.G_tensor = torch.tensor(mult_table, device=self.device)
        
        # Build Reverse signs
        rev_signs = np.zeros(16, dtype=np.float32)
        for i, bi in enumerate(bases):
            rev_bi = ~bi
            # If bi is nonzero, rev_bi.value[i] is either 1 or -1
            # But bi is a standard basis, so bi.value[i] == 1
            rev_signs[i] = rev_bi.value[i]
            
        self.rev_signs = torch.tensor(rev_signs, device=self.device)

    def mul(self, A, B):
        """
        Calculates the pure continuous Geometric Product of two MultiVector grids.
        A and B are tensors of shape [..., 16].
        Returns C = A * B of shape [..., 16].
        """
        # Einsum: A_i * B_j * G_{ijk} -> C_k
        return torch.einsum('...i,...j,ijk->...k', A, B, self.G_tensor)
        
    def rev(self, A):
        """
        Returns the Reversal of MultiVector grid A (~A)
        """
        return A * self.rev_signs
        
    def add(self, A, B):
        return A + B
        
    def sub(self, A, B):
        return A - B

engine = Cl4Engine()
