# Petrophysics-Python-Basics

Small Python programs for petroleum engineering and geoscience. This repo is
the start of a longer goal: applying Python and, later, machine learning to
geology and well data.

## Contents

1. [Darcy's Law Calculator](#1-darcys-law-calculator-darcy_lawpy)
2. [Density Porosity Calculator](#2-density-porosity-calculator-porositypy)

---

## 1. Darcy's Law Calculator (`darcy_law.py`)

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

---

## 2. Density Porosity Calculator (`porosity.py`)

Calculates porosity from bulk density log readings and gives a rough
reservoir quality label for each reading. The calculation is a function
(`density_porosity`) that is reused inside a loop, so several readings can be
processed in one run.

### Formula

φ = (ρ_matrix − ρ_bulk) / (ρ_matrix − ρ_fluid)

| Symbol | Meaning | Unit |
|---|---|---|
| φ | Porosity | fraction (shown as %) |
| ρ_matrix | Matrix (rock grain) density | g/cm³ |
| ρ_bulk | Bulk density from the log | g/cm³ |
| ρ_fluid | Fluid density | g/cm³ |

Typical matrix densities: sandstone 2.65, limestone 2.71, dolomite 2.87 g/cm³.
Typical fluid density: 1.0 g/cm³ (fresh water).

### Quality label (rough cutoffs)

| Porosity | Label |
|---|---|
| above 15% | good |
| 5% to 15% | moderate |
| below 5% | poor |

These cutoffs are approximate, for practice only. Real cutoffs depend on the
reservoir and rock type.

### How to run

```
python porosity.py
```

### Example

Input:

```
matrix density: 2.65
fluid density: 1.0
number of readings: 3
readings: 2.55, 2.45, 2.30
```

Output:

```
rho_b = 2.55 g/cm³  ->  porosity = 6.1%  (moderate)
rho_b = 2.45 g/cm³  ->  porosity = 12.1%  (moderate)
rho_b = 2.30 g/cm³  ->  porosity = 21.2%  (good)
```

Hand check for 2.45: (2.65 − 2.45) / (2.65 − 1.0) = 0.20 / 1.65 = 0.121

### Assumptions

- Clean, fluid-filled rock with a single known matrix density
- The fluid density is known and the same for all readings

### Known limitations

- Shale and gas distort density porosity, and this program does not correct
  for either
- The result depends on the chosen matrix density, so a wrong matrix gives a
  wrong porosity
- If bulk density is above matrix density, the formula would give negative
  porosity, so the program sets it to 0
- Typing letters instead of a number crashes the program (no input
  validation yet)

---

## Planned next

- Input validation with `try/except`
- Reading and plotting real well log (LAS) files

## Author

Gurdeep, B.Tech Petroleum Engineering, PDEU
