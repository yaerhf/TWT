import torch
import numpy as np
import matplotlib.pyplot as plt
import os

print("===================================================================")
print(" TIME-WAVE THEORY: 4D EUCLIDEAN BELL THEOREM SIMULATION")
print("===================================================================")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_bivector_matrix(angle):
    e14 = torch.zeros((len(angle), 4, 4), device=device)
    e14[:, 0, 3] = 1
    e14[:, 3, 0] = -1
    
    e24 = torch.zeros((len(angle), 4, 4), device=device)
    e24[:, 1, 3] = 1
    e24[:, 3, 1] = -1
    
    cos_val = torch.cos(angle).unsqueeze(1).unsqueeze(2)
    sin_val = torch.sin(angle).unsqueeze(1).unsqueeze(2)
    
    return cos_val * e14 + sin_val * e24

def geometric_drag(Psi, D):
    product = torch.bmm(Psi, D)
    trace = product.diagonal(offset=0, dim1=-2, dim2=-1).sum(-1)
    return 0.5 * trace

def simulate_bell_intersection(n_particles=1000000):
    print(f"\nGenerating {n_particles} entangled continuous 4D wave pairs...")
    
    # The 4D phase angle assigned locally at creation
    hidden_lambda = torch.rand(n_particles, device=device) * 2 * np.pi
    
    # 4D Wave forms (Entangled Inverse Bivectors)
    Psi_A = get_bivector_matrix(hidden_lambda)
    Psi_B = -Psi_A 
    
    # Detector A fixed at 0
    theta_A = torch.zeros(n_particles, device=device)
    D_A = get_bivector_matrix(theta_A)
    
    # CONTINUOUS OVERLAP DRAG
    rho_A = geometric_drag(Psi_A, D_A)
    
    # We will track correlations
    del_thetas = np.linspace(0, 2*np.pi, 90)
    continuous_correlations = []
    binary_correlations = []
    
    print("\nSweeping 3D observer plane intersections (Detector B)...")
    
    for dt in del_thetas:
        theta_B = torch.full((n_particles,), dt, device=device, dtype=torch.float32)
        D_B = get_bivector_matrix(theta_B)
        
        rho_B = geometric_drag(Psi_B, D_B)
        
        # 1. THE PRE-THRESHOLD CONTINUOUS MEASUREMENT
        # Calculating Pearson correlation of the raw Topo-Drag Intensities
        # This proves the S3 -> L2 projection is natively sinusoidal
        E_A_centered = rho_A - rho_A.mean()
        E_B_centered = rho_B - rho_B.mean()
        corr_continuous = torch.sum(E_A_centered * E_B_centered) / (torch.sqrt(torch.sum(E_A_centered**2) * torch.sum(E_B_centered**2)))
        continuous_correlations.append(corr_continuous.item())
        
        # 2. THE STRICT BINARY THRESHOLD (The Classical Trap)
        # If we maliciously force the continuous overlap into a binary click without phase-lock logic
        click_A = torch.sign(rho_A)
        click_B = torch.sign(rho_B)
        corr_binary = torch.mean(click_A * click_B).item()
        binary_correlations.append(corr_binary)

    # Plotting
    plt.figure(figsize=(12,7))
    
    # The calculated geometric projection correlation
    plt.plot(np.degrees(del_thetas), continuous_correlations, 'blue', linewidth=3, label='TWT Continuous Projection Correlation')
    plt.plot(np.degrees(del_thetas), binary_correlations, 'orange', linewidth=2, linestyle='--', label='Forced Binary (Classical Bell Limit)')
    
    # The Quantum mechanics target
    quantum_target = -np.cos(del_thetas)
    plt.plot(np.degrees(del_thetas), quantum_target, 'black', linewidth=1, linestyle=':', label='Target Quantum Wave (-cos(θ))')
    
    plt.title("Continuous Topological Drag vs Binary Measurement (Bell Theorem)")
    plt.xlabel("Detector Angle Disparity (Degrees)")
    plt.ylabel("Pearson Correlation")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    os.makedirs("Phase3_Bell_Theorem", exist_ok=True)
    plt.savefig("Phase3_Bell_Theorem/bell_projection_final.png", dpi=300)
    print("\n[SUCCESS] Matrix geometry plotted to Phase3_Bell_Theorem/bell_projection_final.png")
    
    # Explicit Check at 120 Degrees
    theta_120 = torch.full((n_particles,), 2*np.pi/3, device=device)
    rho_120 = geometric_drag(Psi_B, get_bivector_matrix(theta_120))
    
    c_A_cent = rho_A - rho_A.mean()
    c_120_cent = rho_120 - rho_120.mean()
    corr_120_cont = torch.sum(c_A_cent * c_120_cent) / (torch.sqrt(torch.sum(c_A_cent**2) * torch.sum(c_120_cent**2)))
    
    print("\n=========================================================")
    print(" BELL THEOREM DISCREPANCY EVALUATION (Angle = 120 deg)")
    print("=========================================================")
    print(f"Classical Forced-Binary Threshold (Bell Limit)   : +0.333 (1/3)")
    print(f"Expected Quantum Reality (Non-Local Target)      : +0.500 (1/2)")
    print(f"TWT Continuous Matrix Projection                 : {corr_120_cont.item():+.3f}")
    print("=========================================================")

if __name__ == "__main__":
    simulate_bell_intersection()
