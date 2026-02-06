# Equation Solver

A Python program to solve systems of linear equations using NumPy and SciPy.

## Features
- Solves systems of linear equations with any number of variables
- Checks for consistency using rank theorem
- Identifies unique solutions, infinitely many solutions, or no solution

## Requirements
- Python 3.7 or higher
- NumPy
- SciPy

## Installation

### For Users (Windows, macOS, Linux)

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation (Windows)

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program**:
   ```bash
   python equationSolver.py
   ```

## Usage

1. Enter the number of variables in your system
2. For each equation, enter the coefficients and constant term
3. The program will determine if the system has:
   - A unique solution (displays the solution vector)
   - Infinitely many solutions
   - No solution (inconsistent system)

### Example

For the system:
- x₁ + x₂ = 2
- x₁ - x₂ = 0

```
Enter the number of variables: 2

Equation 1:
Enter coefficient of x1: 1
Enter coefficient of x2: 1
Enter the constant: 2

Equation 2:
Enter coefficient of x1: 1
Enter coefficient of x2: -1
Enter the constant: 0

The system is consistent
The system has a unique solution

Solution vector:
[1. 1.]
```

## Creating a Standalone Executable

### On Windows:
```bash
pip install pyinstaller
pyinstaller --onefile equationSolver.py
```
The `.exe` file will be in the `dist/` folder.

### On macOS:
```bash
pip install pyinstaller
pyinstaller --onefile equationSolver.py
```
The executable will be in the `dist/` folder.

## License
Free to use for educational purposes.
