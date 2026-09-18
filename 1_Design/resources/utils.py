def plot_velocity_triangle(U_vec, c_vec, title="Velocity Triangle"):
    """Plots a velocity triangle given U and c vectors. w is calculated automatically."""
    
    import matplotlib.pyplot as plt

    # Calculate w vector as the difference between c and U
    w_vec = [c_vec[0] - U_vec[0], c_vec[1] - U_vec[1]]
    
    plt.figure(figsize=(6,6))
    # Plot U (from origin)
    plt.quiver(0, 0, U_vec[0], U_vec[1], angles='xy', scale_units='xy', scale=1, color='green', label='U')
    # Plot c (from origin)
    plt.quiver(0, 0, c_vec[0], c_vec[1], angles='xy', scale_units='xy', scale=1, color='blue', label='c')
    # Plot w (starts at tip of U, ends at tip of c)
    plt.quiver(U_vec[0], U_vec[1], w_vec[0], w_vec[1], angles='xy', scale_units='xy', scale=1, color='red', label='w')
    
    plt.title(title)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axis('equal')
    plt.show()


def naca65_thickness(x, thickness_ratio):
    """NACA 65-series thickness distribution"""
    import numpy as np
    # Coefficients for NACA 65-series thickness distribution
    a0 = 0.2969
    a1 = -0.1260
    a2 = -0.3516
    a3 = 0.2843
    a4 = -0.1015
    return (thickness_ratio/0.2) * (a0*np.sqrt(x) + a1*x + a2*x**2 + a3*x**3 + a4*x**4)

def circular_arc_camber(x, design_CL):
    """
    CORRECT Circular arc camber line
    design_CL: Target lift coefficient from radial equilibrium
    """
    import numpy as np
    # Convert design CL to maximum camber using thin airfoil theory
    g = design_CL / (2 * np.pi)
    h = g * 0.25  # Maximum camber height at mid-chord

    print(f"Design CL = {design_CL:.3f}")
    print(f"Maximum camber = {h*100:.2f}% of chord")

    # Symmetric airfoil for zero camber
    if h < 1e-6:
        return np.zeros_like(x), np.zeros_like(x)

    # Radius of circular arc
    R = (0.25 + h**2) / (2 * h)

    yc = np.sqrt(np.maximum(R**2 - (x - 0.5)**2, 0)) + h - R

    # Derivative (slope)
    with np.errstate(divide='ignore', invalid='ignore'):
        dyc_dx = (x - 0.5) / np.sqrt(np.maximum(R**2 - (x - 0.5)**2, 1e-12))
        dyc_dx = np.nan_to_num(dyc_dx, nan=0.0, posinf=0.0, neginf=0.0)

    # Calculate leading and trailing edge angles
    le_angle = np.rad2deg(np.arctan(dyc_dx[0]))  # Slope at x=0
    te_angle = np.rad2deg(np.arctan(dyc_dx[-1])) # Slope at x=1

    print(f"Leading edge angle = {le_angle:.2f}°")
    print(f"Trailing edge angle = {te_angle:.2f}°")
    print(f"Circular arc radius = {R:.3f} chord lengths")

    # Verification
    yc_mid = yc[len(yc)//2]  # Camber at mid-chord
    yc_le = yc[0]            # Camber at leading edge
    yc_te = yc[-1]           # Camber at trailing edge

    return yc, dyc_dx

def generate_cambered_airfoil(design_CL, thickness_ratio=0.10, n_points=101):
    """
    Generate complete circular-cambered NACA 65-series airfoil
    """
    print(f"\n{'='*50}")
    print(f"GENERATING AIRFOIL: CL={design_CL:.3f}, thickness={thickness_ratio*100:.1f}%")
    print(f"{'='*50}")
    import numpy as np

    x = np.linspace(0, 1, n_points)

    # Get camber line and thickness
    yc, dyc_dx = circular_arc_camber(x, design_CL)
    yt = naca65_thickness(x, thickness_ratio)

    # Calculate upper and lower surfaces
    theta = np.arctan(dyc_dx)

    x_upper = x - yt * np.sin(theta)
    y_upper = yc + yt * np.cos(theta)

    x_lower = x + yt * np.sin(theta)
    y_lower = yc - yt * np.cos(theta)

    # Combine coordinates
    x_coords = np.concatenate([x_upper[::-1], x_lower[1:]])
    y_coords = np.concatenate([y_upper[::-1], y_lower[1:]])

    airfoil_data = {
        'x_coords': x_coords,
        'y_coords': y_coords,
        'camber_line': yc,
        'thickness_dist': yt,
        'design_CL': design_CL,
        'thickness_ratio': thickness_ratio,
        'name': f'NACA65-C{int(design_CL*100):03d}-{int(thickness_ratio*100):02d}'
    }

    return airfoil_data


def analyze_airfoil_performance(airfoil_data, Re=500000):
    """Simpler version with proper coordinate formatting"""
    print(f"\nAnalyzing {airfoil_data['name']} at Re={Re:.0f}")

    import numpy as np
    import matplotlib.pyplot as plt
    import neuralfoil as nf

    alpha_range = np.linspace(-5, 15, 21)

    # Prepare coordinates: Nx2 array of (x, y) points
    coordinates = np.column_stack([airfoil_data['x_coords'], airfoil_data['y_coords']])

    # Analyze
    results = nf.get_aero_from_coordinates(
        coordinates,
        alpha_range,
        Re,
        model_size="large"
    )

    # Extract results safely
    CL_values = []
    CD_values = []

    for cl, cd in zip(results["CL"], results["CD"]):
        CL_values.append(cl.item() if hasattr(cl, 'item') else float(cl))
        CD_values.append(cd.item() if hasattr(cd, 'item') else float(cd))

    CL_values = np.array(CL_values)
    CD_values = np.array(CD_values)

    # Find actual design angle of attack
    design_alpha = np.interp(airfoil_data['design_CL'], CL_values, alpha_range)

    # Plot results
    plt.figure(figsize=(12, 12))

    plt.subplot(3, 1, 1)
    plt.plot(alpha_range, CL_values, 'b-', linewidth=2)
    plt.axhline(y=airfoil_data['design_CL'], color='r', linestyle='--',
                label=f'Target CL = {airfoil_data["design_CL"]:.2f}')
    plt.axvline(x=design_alpha, color='g', linestyle='--',
                label=f'Design α = {design_alpha:.1f}°')
    plt.xlabel('Angle of Attack α [°]')
    plt.ylabel('Lift Coefficient CL')
    plt.title(f'Lift Curve: {airfoil_data["name"]}')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 2)
    plt.plot(alpha_range, CD_values, 'b-', linewidth=2)
    plt.axvline(x=design_alpha, color='g', linestyle='--',
                label=f'Design α = {design_alpha:.1f}°')
    plt.xlabel('Angle of Attack α [°]')
    plt.ylabel('Drag Coefficient CD')
    plt.title(f'Drag Curve: {airfoil_data["name"]}')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 3)
    plt.plot(alpha_range, np.array(CL_values)/np.array(CD_values), 'g-', linewidth=2)
    plt.xlabel('Angle of Attack α [°]')
    plt.ylabel('Lift-to-Drag Ratio CL/CD')
    plt.title('Aerodynamic Efficiency')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    print(f"Design angle of attack: {design_alpha:.2f}°")
    print(f"CL at design alpha: {np.interp(design_alpha, alpha_range, CL_values):.3f}")

    return design_alpha

def export_onshape_profile(profile, filename=None):
    """
    Export the aerodynamic profile to CSV file to use with Onshape (or any other CAD software).

    Input:
    - profile: Dictionary with nomralized coordinates abd name
    - filename: name for output file. If 'None', the filename is defined with the profile name. It has to have extension .csv
    """
    import csv
    if filename is None:
        filename = profile.get('name', 'perfil_onshape') + '.csv'

    # Put the exension csv if it is missing
    if not filename.endswith('.csv'):
        filename += '.csv'

    x_coords = profile['x_coords']
    y_coords = profile['y_coords']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for x, y in zip(x_coords, y_coords):
            writer.writerow([float(x), float(y), 0.0])

    print(f"✅ Profile '{profile.get('name', 'sin_nombre')}' exported to '{filename}'")
    print(f"   Total points: {len(x_coords)}")
    print(f"   X range: [{min(x_coords):.4f}, {max(x_coords):.4f}]")
    print(f"   Y range: [{min(y_coords):.4f}, {max(y_coords):.4f}]")