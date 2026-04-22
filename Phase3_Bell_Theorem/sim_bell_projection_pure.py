import torch
import numpy as np
import matplotlib.pyplot as plt
import os

print("===================================================================")
print(" TIME-WAVE THEORY: PURE CARTESIAN 4D ISOTROPIC BELL SIMULATION")
print("===================================================================")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_random_4d_bivector(n_particles):
    """
    Generates a pure, random isotropic bivector plane in 4D Cartesian coordinates.
    Zero angles or trigonometric inputs are used.
    """
    # Generate two random Isotropic 4D Vectors
    u = torch.randn(n_particles, 4, device=device)
    w = torch.randn(n_particles, 4, device=device)
    
    # Orthogonalize and Normalize them (Gram-Schmidt) to ensure uniform spherical sampling
    u = torch.nn.functional.normalize(u, p=2, dim=1)
    dot_product = torch.sum(u * w, dim=1, keepdim=True)
    w = w - dot_product * u
    w = torch.nn.functional.normalize(w, p=2, dim=1)
    
    # Mathematical Outer Product (Wedge Product / Commutator Matrix)
    # Bivector Matrix representation: u ^ w = u*w^T - w*u^T
    u_mat = u.unsqueeze(2)
    w_mat = w.unsqueeze(1)
    bivector = torch.bmm(u_mat, w_mat) - torch.bmm(w_mat.transpose(1, 2), u.unsqueeze(1))
    
    # The normalization factor for simple bivectors of orthogonal unit vectors is 1,
    # but we will strictly normalize it mechanically to norm=1
    trace = torch.diagonal(torch.bmm(bivector, bivector), dim1=-2, dim2=-1).sum(-1)
    norm = torch.sqrt(-0.5 * trace).unsqueeze(1).unsqueeze(2)
    bivector = bivector / torch.clamp(norm, min=1e-8)
    
    return bivector

def get_detector_bivector(theta):
    """
    The detector is a macroscopic physical plane intersecting the 4th spatial axis.
    The macroscopic observer points their laboratory axis along theta.
    The detector bivector is: (Observer_Axis) ^ (Temporal_Axis)
    """
    n_particles = len(theta)
    
    # Observer Axis in their 3D macroscopic limit (X-Y plane of the lab)
    obs_axis = torch.zeros(n_particles, 4, device=device)
    obs_axis[:, 0] = torch.cos(theta)
    obs_axis[:, 1] = torch.sin(theta)
    
    # The Time-Wave propagation axis
    temporal_axis = torch.zeros(n_particles, 4, device=device)
    temporal_axis[:, 3] = 1.0  # e_4 direction
    
    # Detector Bivector Subspace: obs_axis ^ temporal_axis
    obs_mat = obs_axis.unsqueeze(2)
    temp_mat = temporal_axis.unsqueeze(1)
    
    D = torch.bmm(obs_mat, temp_mat) - torch.bmm(temporal_axis.unsqueeze(2), obs_axis.unsqueeze(1))
    return D

def geometric_drag(Psi, D):
    """
    Calculates the continuous Frobenius topological overlap (Phase Elasticity mapping).
    """
    product = torch.bmm(Psi, D)
    trace = product.diagonal(offset=0, dim1=-2, dim2=-1).sum(-1)
    return 0.5 * trace

def simulate_pure_cartesian_bell(n_particles=1000000):
    print(f"\nGenerating {n_particles} Angle-Free Isotropic 4D Particle waves...")
    
    # 4D Wave forms (Entangled Geometries, literally just coordinate subspaces)
    Psi_A = get_random_4d_bivector(n_particles)
    Psi_B = -Psi_A  # Exact inverse coordinate geometry
    
    # Detector A fixed at macroscopic angle 0
    theta_A = torch.zeros(n_particles, device=device)
    D_A = get_detector_bivector(theta_A)
    rho_A = geometric_drag(Psi_A, D_A)
    
    del_thetas = np.linspace(0, 2*np.pi, 90)
    continuous_correlations = []
    
    print("\nSweeping 3D observer plane intersections (Detector B)...")
    
    for dt in del_thetas:
        theta_B = torch.full((n_particles,), dt, device=device, dtype=torch.float32)
        D_B = get_detector_bivector(theta_B)
        
        rho_B = geometric_drag(Psi_B, D_B)
        
        # PRE-THRESHOLD CONTINUOUS MEASUREMENT
        # Calculating Pearson correlation of the pure Topological Drag Intensities
        E_A_centered = rho_A - rho_A.mean()
        E_B_centered = rho_B - rho_B.mean()
        corr_continuous = torch.sum(E_A_centered * E_B_centered) / (torch.sqrt(torch.sum(E_A_centered**2) * torch.sum(E_B_centered**2)))
        
        continuous_correlations.append(corr_continuous.item())

    # Plotting
    plt.figure(figsize=(12,7))
    
    plt.plot(np.degrees(del_thetas), continuous_correlations, 'blue', linewidth=3, label='Pure Cartesian 4D Isotropic Projection (TWT)')
    
    # The Quantum mechanics target
    quantum_target = -0.5 * np.cos(del_thetas) # Wait, correlation for continuous variables usually maps directly proportional to cos
    # Let's see what the pure math naturally projects to without forcing a quantum line. We will plot cosine for scale.
    normalized_quantum_target = -np.cos(del_thetas)
    
    # We will normalize the array to peak correlation amplitude to see if the SHAPE matches
    peak_corr = np.max(np.abs(continuous_correlations))
    plt.plot(np.degrees(del_thetas), normalized_quantum_target * peak_corr, 'red', linestyle='--', linewidth=2, label='Quantum Target Shape (Cos)')
    
    plt.title("Pure Isotropic Cartesian Projection vs Quantum Non-Locality")
    plt.xlabel("Detector Angle Disparity (Degrees)")
    plt.ylabel("Pearson Correlation")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    os.makedirs("Phase3_Bell_Theorem", exist_ok=True)
    plt.savefig("Phase3_Bell_Theorem/bell_pure_cartesian_plot.png", dpi=300)
    print("\n[SUCCESS] Matrix geometry plotted to Phase3_Bell_Theorem/bell_pure_cartesian_plot.png")
    
    # Evaluation at exactly 120 Degrees (Quantum limit check vs triangular)
    theta_120 = torch.full((n_particles,), 2*np.pi/3, device=device)
    rho_120 = geometric_drag(Psi_B, get_detector_bivector(theta_120))
    c_120_cent = rho_120 - rho_120.mean()
    corr_120_cont = torch.sum(E_A_centered * c_120_cent) / (torch.sqrt(torch.sum(E_A_centered**2) * torch.sum(c_120_cent**2)))
    
    base_corr = np.max(np.abs(continuous_correlations))
    # Standard classical triangular boundary would be at 0.33 of the peak!
    
    print("\n=========================================================")
    print(" BELL THEOREM DISCREPANCY EVALUATION (Angle = 120 deg)")
    print("=========================================================")
    print(f"Base Maximum Projection Correlation Amplitude      : {base_corr:+.3f}")
    print(f"Target Expectation (0.5 * Peak)                  : {base_corr * 0.5:+.3f}")
    print(f"TWT Pure Cartesian Matrix Projection Outline     : {corr_120_cont.item():+.3f}")
    print("=========================================================")

if __name__ == "__main__":
    simulate_pure_cartesian_bell()
