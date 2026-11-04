# Petrophysics-Python-Basics

Python programs for petroleum engineering and geoscience. This repo is the
start of a longer goal: applying Python and, later, machine learning to
geology and well data.

## Darcy's Law Calculator (`darcy_law.py`)

Calculates the volumetric flow rate through a saturated porous medium and
reports the flow direction.

### Formula

Q = -K * A * (h2 - h1) / L

| Symbol | Meaning | Unit |
|---|---|---|
| Q | Volumetric flow rate | m³/s |
| K | Hydraulic conductivity | m/s |
| A | Cross-sectional area | m² |
| L | Length of flow path | m |
| h1 | Head at the start of the flow path | m |
| h2 | Head at the end of the flow path | m |

Q > 0: flow from h1 to h2 (head decreasing). Q < 0: flow from h2 to h1.
Q = 0: no flow.

### How to run

```
python darcy_law.py
```

### Example

Input: K = 2, A = 3, L = 4, h2 = 5, h1 = 6

Output:

```
the value of Q is: 1.5
the flow is from h1 to h2 (head decreasing direction)
```

Hand check: Q = -(2 × 3 × (5 - 6)) / 4 = 1.5

### Assumptions

- Laminar, steady-state, single-phase flow
- Homogeneous, saturated porous medium
- One-dimensional flow

### Known limitations

- Typing letters instead of a number crashes the program (no input
  validation yet)
- Only the hydraulic conductivity form of Darcy's law is implemented, not
  the permeability form (k in mD with fluid viscosity)
- Does not handle multiphase flow, which is the usual case in real reservoirs
- Units are not enforced: the user must enter consistent SI units

## Planned next

- Input validation with `try/except`
- Porosity from a density log
- Reading and plotting real well log (LAS) files

## Author

Gurdeep, B.Tech Petroleum Engineering, PDEU