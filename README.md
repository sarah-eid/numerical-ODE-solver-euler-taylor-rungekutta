# Numerical Solutions for Ordinary Differential Equations

## Project Overview

This repository contains a comprehensive implementation and analysis of three classical numerical methods for solving first-order Ordinary Differential Equations (ODEs). The project solves the initial value problem:

`dy/dx = 3e^(2x)y, with y(0) = 1 and y(0) = 0.5`

using **Euler's Method**, **Taylor's Method (2nd Order)**, and **Runge-Kutta Method (6th Order)**. The implementation includes Python code, detailed numerical comparisons, visualizations, and a complete project report.

## Repository Structure

```
Numerical-ODE-Solver/
├── src/
│   ├── Numerical_Code_2.py    # y(0)=1, x=0→1, detailed output
│   └── FinalNum_1.py          # y(0)=0.5, x=0→0.5, concise version
├── report/
│   └── FinalProjectNum.pdf    # Complete project report
└── README.md                  # This file
```

## Implementation Details

### Methods Implemented

1. **Euler's Method**
   - First-order explicit method
   - Simple but less accurate
   - Formula: \( y_{n+1} = y_n + h f(x_n, y_n) \)

2. **Taylor's Method (2nd Order)**
   - Incorporates second derivative information
   - Improved accuracy over Euler
   - Formula: \( y_{n+1} = y_n + h f + \frac{h^2}{2} f' \)

3. **Runge-Kutta Method (6th Order)**
   - High-accuracy method with six function evaluations
   - Closely matches exact solution
   - Weighted average of slopes: \( \frac{7k_1 + 32k_3 + 12k_4 + 32k_5 + 7k_6}{90} \)

### Problem Specifications

**Case 1** (`Numerical_Code_2.py`):
- Initial condition: \( y(0) = 1 \)
- Domain: \( x \in [0, 1] \)
- Step size: \( h = 0.05 \)
- Steps: 20

**Case 2** (`FinalNum_1.py`):
- Initial condition: \( y(0) = 0.5 \)
- Domain: \( x \in [0, 0.5] \)
- Step size: \( h = 0.05 \)
- Steps: 10

## Results and Analysis

### Accuracy Comparison
| Method | Order | Accuracy | Computational Cost |
|--------|-------|----------|-------------------|
| Euler | 1st | Low | Low |
| Taylor | 2nd | Medium | Medium |
| Runge-Kutta 6 | 6th | High | High |

### Key Findings
- **Runge-Kutta 6th order** provides the closest approximation to the exact solution
- **Euler's method** shows significant error accumulation over time
- **Taylor's method** offers a good balance between simplicity and accuracy
- All methods diverge from exact solution as \( x \) increases due to the exponential nature of the ODE

## Getting Started

### Prerequisites
- Python 3.6+
- matplotlib

### Running the Code
```bash
# Run detailed version (y(0)=1, x=0→1)
python src/Numerical_Code_2.py

# Run concise version (y(0)=0.5, x=0→0.5)
python src/FinalNum_1.py
```

## Sample Output

### Numerical Results Table
```
    x |     Euler |    Taylor |       RK6 |     Exact
------------------------------------------------------------
  0.00 |   1.000000 |  1.000000 |  1.000000 |  1.000000
  0.05 |   1.150000 |  1.168750 |  1.170880 |  1.170880
  0.10 |   1.340641 |  1.388248 |  1.393898 |  1.393898
  ... |        ... |       ... |       ... |       ...
  1.00 |  37.213232 | 77.158777 | 86.713695 | 86.713696
```


## Contributors

- Sarah Eid | [Judy Abuquta](https://github.com/JudyAbuquta) | [Abeer Hussain](https://github.com/abeerahrar) 

---

**Tags** :`numerical-methods`, `ordinary-differential-equations`, `runge-kutta`, `euler-method`, `taylor-series`, `python`, `computational-mathematics`, `ode-solver`
