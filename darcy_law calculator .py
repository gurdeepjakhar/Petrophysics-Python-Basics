def darcy_law():
    """Calculate flow rate Q (m³/s) using Darcy's law: Q = -K*A*(h2-h1)/L
    Assumes laminar, steady, single-phase flow in saturated porous media.
    Units: K (m/s), A (m²), L, h1, h2 (m).
    """
    K = float(input("enter the hydraulic conductivity K (m/s): "))
    A = float(input("enter the cross sectional area A (m²): "))
    L = float(input("enter the length of the flow path L (m): "))
    h2 = float(input("enter the head at the end h2 (m): "))
    h1 = float(input("enter the head at the start h1 (m): "))
    if L <= 0:
        print("the length of the flow path must be positive")
        return None
    Q = -K*A*(h2-h1)/L
    print("the value of Q is:", Q, "m³/s")
    if Q == 0:
        print("there is no flow")
    elif Q < 0:
        print("the flow is from h2 to h1 (head increasing direction)")
    else:
        print("the flow is from h1 to h2 (head decreasing direction)")
    return Q

darcy_law()