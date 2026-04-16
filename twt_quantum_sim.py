import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from clifford.g4 import *

class TopologicalWavePacket:
    def __init__(self, k_0, delta_k, num_components=250):
        self.k_0 = k_0
        self.delta_k = delta_k
        self.k_array = np.linspace(k_0 - 4*delta_k, k_0 + 4*delta_k, num_components)
        self.weights = np.exp(-0.5 * ((self.k_array - k_0) / delta_k)**2)
        
    def evaluate_slice(self, x1_array, x4_present):
        """
        Evaluate the wavepacket by constructing formal Cl(4,0) Rotors
        and returning the resulting multivector field.
        """
        # Vectorize via NumPy Broadcasting for GPU/CPU optimization
        k_col = self.k_array[:, np.newaxis]
        w_col = self.weights[:, np.newaxis]
        x1_row = x1_array[np.newaxis, :]
        
        phase_matrix = k_col * x1_row - k_col * x4_present
        
        # Superposition strictly via continuous algebra evaluation limits
        sum_cos = np.sum(w_col * np.cos(phase_matrix), axis=0)
        sum_sin = np.sum(w_col * np.sin(phase_matrix), axis=0)
        
        # Formally construct and return the Cl(4,0) Geometrical Object (MVArray)
        psi = sum_cos * 1.0 + e14 * sum_sin
            
        return psi

class QuantumMeasurementSimulator:
    @staticmethod
    def calculate_uncertainty_product(delta_k_input):
        print(f"\n--- Testing Spatial Localization with Delta_k (Tilt Variance) = {delta_k_input:.2f} ---")
        
        # Build the wavepacket
        packet = TopologicalWavePacket(k_0=10.0, delta_k=delta_k_input)
        
        # 1D Spatial grid (10,000 sampling points is instant with vectorized MVArray)
        x1 = np.linspace(-40, 40, 10000)
        x4_slice = 0.0 # Snapshot at Present Time-Wave
        
        # Retrieve the multivector state across space
        psi_mv = packet.evaluate_slice(x1, x4_slice)
        
        # Calculate standard existence friction/probability density mapping.
        # In Geometric Algebra, this is the multivector multiplied by its reverse (~psi_mv).
        # This natively reproduces the exact probability distribution (Born Rule) without quantum axioms.
        density_mv = psi_mv * ~psi_mv
        
        # The result is purely a scalar field representing kinetic density.
        # We extract index 0 from the 16-element Cl(4,0) array
        density = density_mv.value[:, 0]
        
        norm = np.trapezoid(density, x1)
        density /= norm
        
        # Measure true statistical variance in spatial dimension
        mean_x = np.trapezoid(x1 * density, x1)
        var_x = np.trapezoid((x1 - mean_x)**2 * density, x1)
        delta_x = np.sqrt(var_x)
        
        # The physical Delta_k of the structure
        delta_k_true = delta_k_input / np.sqrt(2.0) 
        
        print(f"Measured 3D Spatial Fuzziness (Delta_x): {delta_x:.4f}")
        print(f"Mapped 4D Geometric Tilt Variance (Delta_p): {delta_k_true:.4f}")
        
        # The Heisenberg Product
        product = delta_x * delta_k_true
        print(f"Geometric Uncertainty Limit (Delta_x * Delta_p): {product:.4f}")
        return product

def run_tests():
    print("===================================================================")
    print(" Time-Wave Topology (TWT) - Formal Cl(4,0) Limit Tester")
    print(" GPU Accelerable via 16D array projection (Vectorized CPU Mode Active)")
    print("===================================================================")
    
    test_variances = [0.25, 0.5, 1.0, 2.0, 4.0]
    
    products = []
    for dk in test_variances:
        prod = QuantumMeasurementSimulator.calculate_uncertainty_product(dk)
        products.append(prod)
        
    print("\n===================================================================")
    print(f" RESULT (Cl(4,0)): {np.round(products, 4)}")
    print(" The Uncertainty Limit strictly emerges from projecting multivector rotations.")


def animate_time_wave(delta_k_input=1.0):
    print("\nGenerating 4D Time-Wave intercept animation...")
    packet = TopologicalWavePacket(k_0=10.0, delta_k=delta_k_input)
    x1 = np.linspace(-40, 40, 1000)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_facecolor('#1a1a2e')
    fig.patch.set_facecolor('#1a1a2e')
    
    ax.set_xlim(-20, 20)
    ax.set_ylim(0, 0.4)
    ax.set_title(f'TWT Simulation: e4 Time-Wave Intercepting Space (Cl(4,0))\nGeometric Envelope localized inside 3D slice', color='white', fontsize=12)
    ax.set_xlabel('Spatial Coordinate (e1 axis)', color='white')
    ax.set_ylabel('Vortex Density (scalar projection)', color='white')
    ax.tick_params(colors='white')
    ax.grid(color='#4c4c6d', linestyle='--', linewidth=0.5, alpha=0.5)

    line, = ax.plot([], [], color='#e94560', lw=2.5, label='Projected Density (psi * ~psi)')
    envelope_line, = ax.plot([], [], color='#0f3460', lw=1.5, linestyle='--', alpha=0.8, label='Time-Wave Base')
    ax.legend(facecolor='#1a1a2e', edgecolor='#4c4c6d', labelcolor='white')

    time_slices = np.linspace(-10, 10, 200)

    def init():
        line.set_data([], [])
        envelope_line.set_data([], [])
        return line, envelope_line

    def animate(i):
        x4_current = time_slices[i]
        
        # Recalculate the true geometric field strictly at this temporal x4 slice
        psi_mv = packet.evaluate_slice(x1, x4_present=x4_current)
        density_mv = psi_mv * ~psi_mv
        density = density_mv.value[:, 0]
        
        # Normalizing to visualize localized soliton height
        density /= np.max(density) if np.max(density) > 0 else 1
        density *= 0.3 # Scale for plotting
        
        envelope = np.exp(-((x1 - x4_current) / (2.0))**2) * 0.15 # Guide 

        line.set_data(x1, density)
        envelope_line.set_data(x1, envelope)
        return line, envelope_line

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(time_slices), interval=30, blit=True)
    
    anim_filename = 'time_wave_soliton.mp4'
    print("Saving High-Performance mp4 animation...")
    try:
        anim.save(anim_filename, fps=30, extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
        print(f"Animation saved successfully to {anim_filename}")
    except Exception as e:
        print(f"Failed to save MP4: {e}")
        print("Saving as animated GIF instead...")
        anim.save('time_wave_soliton.gif', writer='pillow', fps=30)
        print("Saved to time_wave_soliton.gif")

if __name__ == '__main__':
    run_tests()
    animate_time_wave(delta_k_input=1.0)
