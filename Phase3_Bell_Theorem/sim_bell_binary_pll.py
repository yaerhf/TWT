import torch
import numpy as np
import matplotlib.pyplot as plt
import os

print("===================================================================")
print(" TIME-WAVE THEORY: BINARY PHASE-LOCKED LOOP (CHSH TEST)")
print("===================================================================")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_random_4d_bivector(n_particles):
    u = torch.randn(n_particles, 4, device=device)
    w = torch.randn(n_particles, 4, device=device)
    
    u = torch.nn.functional.normalize(u, p=2, dim=1)
    dot_product = torch.sum(u * w, dim=1, keepdim=True)
    w = w - dot_product * u
    w = torch.nn.functional.normalize(w, p=2, dim=1)
    
    u_mat = u.unsqueeze(2)
    w_mat = w.unsqueeze(1)
    bivector = torch.bmm(u_mat, w_mat) - torch.bmm(w_mat.transpose(1, 2), u.unsqueeze(1))
    
    trace = torch.diagonal(torch.bmm(bivector, bivector), dim1=-2, dim2=-1).sum(-1)
    norm = torch.sqrt(-0.5 * trace).unsqueeze(1).unsqueeze(2)
    bivector = bivector / torch.clamp(norm, min=1e-8)
    
    return bivector

def get_detector_bivector(theta):
    n_particles = len(theta)
    obs_axis = torch.zeros(n_particles, 4, device=device)
    obs_axis[:, 0] = torch.cos(theta)
    obs_axis[:, 1] = torch.sin(theta)
    
    temporal_axis = torch.zeros(n_particles, 4, device=device)
    temporal_axis[:, 3] = 1.0
    
    obs_mat = obs_axis.unsqueeze(2)
    temp_mat = temporal_axis.unsqueeze(1)
    
    D = torch.bmm(obs_mat, temp_mat) - torch.bmm(temporal_axis.unsqueeze(2), obs_axis.unsqueeze(1))
    return D

def geometric_drag(Psi, D):
    product = torch.bmm(Psi, D)
    trace = product.diagonal(offset=0, dim1=-2, dim2=-1).sum(-1)
    return 0.5 * trace

def compute_chsh_for_threshold(threshold, n_particles=5000000):
    # CHSH Angles
    # Bell optical tests generally use 0, 45, 90, 135 offsets depending on basis
    # A standard CHSH setup uses a=0, a'=pi/2 (90), b=pi/4 (45), b'=3pi/4 (135)
    angles = {
        'a': 0.0,
        'a_prime': np.pi / 2,
        'b': np.pi / 4,
        'b_prime': 3 * np.pi / 4
    }
    
    Psi_A = get_random_4d_bivector(n_particles)
    Psi_B = -Psi_A 
    
    def get_correlations(angle_A, angle_B):
        theta_A = torch.full((n_particles,), angle_A, device=device, dtype=torch.float32)
        theta_B = torch.full((n_particles,), angle_B, device=device, dtype=torch.float32)
        
        D_A = get_detector_bivector(theta_A)
        D_B = get_detector_bivector(theta_B)
        
        rho_A = geometric_drag(Psi_A, D_A)
        rho_B = geometric_drag(Psi_B, D_B)
        
        # STRICT INDEPENDENT LOCAL THRESHOLDING
        # Representing an atomic detector requiring geometric intersection limits to click
        click_A = (torch.abs(rho_A) > threshold).float() * torch.sign(rho_A)
        click_B = (torch.abs(rho_B) > threshold).float() * torch.sign(rho_B)
        
        valid = (click_A != 0) & (click_B != 0)
        if valid.sum() > 0:
            corr = torch.mean(click_A[valid] * click_B[valid]).item()
            efficiency = (valid.sum().float() / n_particles).item()
        else:
            corr = 0
            efficiency = 0
            
        return corr, efficiency

    E_ab, eff_ab = get_correlations(angles['a'], angles['b'])
    E_ab_prime, _ = get_correlations(angles['a'], angles['b_prime'])
    E_a_prime_b, _ = get_correlations(angles['a_prime'], angles['b'])
    E_a_prime_b_prime, _ = get_correlations(angles['a_prime'], angles['b_prime'])
    
    # S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')|
    # Adjusting signs for correlation direction standard
    S = abs(E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime)
    return S, eff_ab

def sweep_thresholds():
    thresholds = np.linspace(0.0, 0.95, 20)
    S_values = []
    efficiencies = []
    
    print(f"\nSweeping strictly local atomic thresholds to extract CHSH S Parameter...")
    for t in thresholds:
        S, eff = compute_chsh_for_threshold(t)
        S_values.append(S)
        efficiencies.append(eff)
        print(f"Threshold: {t:.2f} | Efficiency: {eff*100:6.2f}% | CHSH S: {S:.4f}")
        
    fig, ax1 = plt.subplots(figsize=(10,6))

    color = 'tab:red'
    ax1.set_xlabel('Geometric Phase-Lock Threshold (T)')
    ax1.set_ylabel('CHSH Parameter (S)', color=color)
    ax1.plot(thresholds, S_values, color=color, linewidth=3)
    ax1.axhline(y=2.0, color='black', linestyle='--', label='Classical Local Bound (S=2)')
    ax1.axhline(y=2.83, color='grey', linestyle=':', label='Quantum Tsirelson Bound (S=2.83)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='lower left')

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Coincidence Detection Efficiency', color=color)  
    ax2.plot(thresholds, efficiencies, color=color, linestyle='--')
    ax2.axhline(y=0.82, color='blue', linestyle=':', label='2015 Loophole-Free Limit (82%)')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title("CHSH Parameter vs Independent Local Projection Thresholding")
    
    os.makedirs("Phase3_Bell_Theorem", exist_ok=True)
    plt.savefig("Phase3_Bell_Theorem/bell_binary_chsh.png", dpi=300)
    print("\n[SUCCESS] CHSH Plot saved to Phase3_Bell_Theorem/bell_binary_chsh.png")

if __name__ == "__main__":
    sweep_thresholds()
