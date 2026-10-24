def fixed_point_iteration(g, p_0, approximation_tolerance, max_iterations):
    """
    Approximate a fixed point of g using fixed-point iteration.

    Parameters:
        g: function
        p_0: initial guess
        approximation_tolerance: stopping tolerance
        max_iterations: maximum number of iterations

    Returns:
        A list of iterates if convergence occurs,
        otherwise a failure message.
    """
    p_list = [p_0]
    p_n = p_0

    for _ in range(max_iterations):
        p_temp = g(p_n)
        p_list.append(p_temp)

        if abs(p_temp - p_n) < approximation_tolerance:
            return p_list

        p_n = p_temp

    return f"Fixed-point iteration failed to converge in {max_iterations} iterations."