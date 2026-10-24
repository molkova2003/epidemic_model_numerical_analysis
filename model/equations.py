import numpy as np


def f(x, R_0=2.5):
    """Root-finding function for Newton's method."""
    return x - 1 + np.exp(-R_0 * x)


def f_prime(x, R_0=2.5):
    """Derivative of f."""
    return 1 - R_0 * np.exp(-R_0 * x)


def g(x, R_0=2.5):
    """Fixed-point function."""
    return 1 - np.exp(-R_0 * x)


def g_prime(x, R_0=2.5):
    """Derivative of g."""
    return R_0 * np.exp(-R_0 * x)


def f_vac(x, v, R_0=2.5):
    """Vaccination-adjusted root-finding function."""
    return x - (1 - v) * (1 - np.exp(-R_0 * x))


def f_prime_vac(x, v, R_0=2.5):
    """Derivative of vaccination-adjusted root-finding function."""
    return 1 - (1 - v) * R_0 * np.exp(-R_0 * x)


def g_vac(x, v, R_0=2.5):
    """Vaccination-adjusted fixed-point function."""
    return (1 - v) * (1 - np.exp(-R_0 * x))