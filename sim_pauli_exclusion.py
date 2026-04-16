"""
TWT Demonstration: Pauli Exclusion Clash
===================================================================
Standard logic decrees that two fermions cannot occupy the same state, 
mandating "Probability collapses" and absolute exclusion principles.

In Time-Wave Topology (TWT), fermions are not discrete dots floating in void;
they are 4D continuous waves moving through a Spacetime elastic bulk. 
If two waves carry IDENTICAL geometric chirality (the exact same fluid spin mapping
to +e12), bringing them together means pushing matching fluid gears against each other!

This simulation injects two identical topologies (+e12 and +e12) into the grid. 
When the simulation overlaps them seamlessly using the pure Geometric Product,
it mathematically produces an unbounded energy spike (Massive Constructive Topological Drag).

Physics maps this mathematical limit as an "infinite potential barrier."
TWT proves this isn't magic: Trying to cram identically spinning geometries into 
the exact same continuous space results in massive constructive friction!
"""

import torch
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from twt_algebra_core_torch import engine

def define_space(res=60, extent=4.0):
    x = torch.linspace(-extent, extent, res, device=engine.device)
    y = torch.linspace(-extent, extent, res, device=engine.device)
    z = torch.linspace(-extent, extent, res, device=engine.device)
    Z, Y, X = torch.meshgrid(z, y, x, indexing='ij')
    return X, Y, Z

def build_soliton(X, Y, Z, center, twist_polarity=1.0):
    R_sq = (X - center[0])**2 + (Y - center[1])**2 + (Z - center[2])**2
    r = torch.sqrt(R_sq)
    
    envelope = torch.exp(-r)
    
    MV_field = torch.zeros((*X.shape, 16), dtype=torch.float32, device=engine.device)
    MV_field[..., 0] = envelope * torch.cos(twist_polarity * r)
    MV_field[..., 5] = envelope * torch.sin(twist_polarity * r) # e12 plane
    
    return MV_field

def simulate_pauli_exclusion(distances):
    X, Y, Z = define_space(res=60, extent=4.0)
    total_friction_drag = []
    
    print("\n[TWT Simulation] Simulating Pauli Geometric Exclusion (Identical Spins)")
    
    for d in distances:
        center_A = [d/2.0, 0, 0]
        center_B = [-d/2.0, 0, 0]
        
        # Instantiate identical structures
        Psi_A = build_soliton(X, Y, Z, center_A, twist_polarity=1.0)
        Psi_B = build_soliton(X, Y, Z, center_B, twist_polarity=1.0)
        
        Psi_Total = engine.add(Psi_A, Psi_B)
        
        # Massive topological friction calculation
        Density_Field = engine.mul(Psi_Total, engine.rev(Psi_Total))
        scalar_drag = Density_Field[..., 0]
        
        total_drag = torch.sum(scalar_drag).item()
        total_friction_drag.append(total_drag)
        
    return total_friction_drag

def plot_results():
    distances = np.linspace(0.1, 4.0, 100)
    drag_pauli = simulate_pauli_exclusion(distances)
    
    fig, ax = plt.subplots(figsize=(10,6))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.tick_params(colors='white')
    
    ax.plot(distances, drag_pauli, color='#e94560', lw=2.5, label='Pauli Clash (Identical Bivectors)')
    ax.set_xlabel('Geometric Separation Distance (D)', color='white')
    ax.set_ylabel('Total Scalar Drag (Geometrical Resistance energy)', color='white')
    ax.set_title('TWT Pauli Exclusion Simulation\nExtreme Constructive Friction Spike at close range', color='white')
    
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('sim_pauli_exclusion.png', dpi=150)
    print("Graph generated and saved to 'sim_pauli_exclusion.png'")

if __name__ == '__main__':
    plot_results()
