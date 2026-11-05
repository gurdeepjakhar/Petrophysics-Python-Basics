def density_porosity(rho_bulk, rho_matrix, rho_fluid):
    """Porosity from a bulk density log reading (g/cm³).

    phi = (rho_matrix - rho_bulk) / (rho_matrix - rho_fluid)
    Returns porosity as a fraction, or None if inputs are invalid.
    """
    if rho_bulk <= 0 or rho_matrix <= 0 or rho_fluid <= 0:
        print("densities must be positive values")
        return None
    if rho_matrix == rho_fluid:
        print("matrix and fluid density cannot be equal")
        return None

    phi = (rho_matrix - rho_bulk) / (rho_matrix - rho_fluid)

    if phi < 0:      
        phi = 0
    return phi


def quality_label(phi):
    """Rough reservoir quality label (cutoffs are approximate)."""
    if phi > 0.15:
        return "good"
    elif phi >= 0.05:
        return "moderate"
    else:
        return "poor"
    
rho_matrix = float(input("enter the matrix density (g/cm³): "))
rho_fluid = float(input("enter the fluid density (g/cm³): "))
n = int(input("how many bulk density readings do you have? "))

for i in range(n):
    rho = float(input(f"enter bulk density reading {i + 1} (g/cm³): "))
    phi = density_porosity(rho, rho_matrix, rho_fluid)
    if phi is not None:
        print(f"rho_b = {rho:.2f} g/cm³  ->  porosity = {phi:.1%}  ({quality_label(phi)})")