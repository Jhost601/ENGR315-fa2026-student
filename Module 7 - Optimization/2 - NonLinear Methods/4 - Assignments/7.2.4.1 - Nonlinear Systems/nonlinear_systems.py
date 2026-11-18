"""ENGR 315 | Nonlinear Systems Assignment

Complete the four functions below. Do not change their names, parameters,
or return types. Submit this file to Gradescope.

You may use NumPy and SciPy. Do not hard-code the final dimensions.
"""
import numpy as np
from scipy.optimize import root


def residuals(dimensions):
    """Return a NumPy array of shape (2,) with [f1, f2]."""
    
    x, y = dimensions
    f1 = x**2 + y**2 - 41
    f2 = x + y - 9

    
    # TODO (20 points): implement the nonlinear equations.
    return np.array([f1, f2], dtype=float)


def jacobian(dimensions):
    """Return a NumPy array of shape (2, 2) containing the Jacobian."""
    x, y = dimensions

    J = np.array([
        [2*x, 2*y],
        [1, 1]
    ])
    # TODO (20 points): implement the Jacobian matrix.
    return J


def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=50):
    """Return a NumPy array of shape (2,) with the converged dimensions.

    Use a for loop and np.linalg.solve(J, -F). Stop when the maximum
    absolute residual is strictly smaller than tolerance. If the solver
    does not converge within max_iterations, raise RuntimeError.
    """
    dimensions = np.array(initial_guess, dtype=float)

    for i in range(max_iterations):
        F = residuals(dimensions)

        # Check if the solution has converged
        if np.max(np.abs(F)) < tolerance:
            return dimensions

        # Calculate Jacobian
        J = jacobian(dimensions)

        # Solve for the change in dimensions
        delta = np.linalg.solve(J, -F)

        # Update dimensions
        dimensions = dimensions + delta

    # Check convergence after the final update
    if np.max(np.abs(residuals(dimensions))) < tolerance:
        return dimensions

    # TODO (40 points): implement the iterative Newton-Raphson algorithm.
    return RuntimeError("Newton-Raphson did not converge")


def solve_scipy(initial_guess):
    """Return a NumPy array of shape (2,) using scipy.optimize.root.

    Check solution.success. Raise RuntimeError if the solver fails.
    """
    solution = root(residuals, initial_guess, jac=jacobian)

    if not solution.success:
        raise RuntimeError("SciPy solver failed")
    # TODO (20 points): use root() to solve the system.
    return solution.x



if __name__ == "__main__":
    guess = np.array([3.0, 6.0])
    print("Initial guess:", guess)
    print("Residuals at guess:", residuals(guess))
    print("Jacobian at guess:\n", jacobian(guess))
    print("NumPy Newton-Raphson:", newton_raphson(guess))
    print("SciPy root:", solve_scipy(guess))
