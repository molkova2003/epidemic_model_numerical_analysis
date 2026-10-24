import numpy as np


def empirical_order(p_list):
    """
    Compute empirical order of convergence for an iterative method.
    """
    a_list = []
    p = p_list[-1]

    for i in range(len(p_list) - 2):
        numerator = np.log(abs(p_list[i + 2] - p) / abs(p_list[i + 1] - p))
        denominator = np.log(abs(p_list[i + 1] - p) / abs(p_list[i] - p))
        a_temp = numerator / denominator

        if np.isfinite(a_temp):
            a_list.append(a_temp)
        else:
            return a_list

    return a_list


def asymptotic_constant(p_list):
    """
    Compute asymptotic convergence constant for a linearly convergent method.
    """
    c_list = []
    p = p_list[-1]

    for i in range(len(p_list) - 2):
        c_temp = abs(p_list[i + 1] - p) / abs(p_list[i] - p)

        if np.isfinite(c_temp):
            c_list.append(c_temp)
        else:
            return c_list

    return c_list