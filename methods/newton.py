def newtons_method(f, f_prime, p_0, approximation_tolerance, max_iterations):
    """
    Approximate a root of f using Newton's method.

    Parameters:
        f: function
        f_prime: derivative of f
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
        p_temp = p_n - f(p_n) / f_prime(p_n)
        p_list.append(p_temp)

        if abs(p_temp - p_n) < approximation_tolerance:
            return p_list

        p_n = p_temp

    return f"Newton's method failed to converge in {max_iterations} iterations."