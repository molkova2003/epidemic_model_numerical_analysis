from methods.newton import newtons_method
from methods.fixed_point import fixed_point_iteration
from model.equations import f, f_prime, g, g_prime, f_vac, f_prime_vac
from utils.format_output import format_table
from analysis.convergence import empirical_order, asymptotic_constant


def main():
    # Basic reproduction number R_0 = 2.5
    p_list = newtons_method(f, f_prime, 1, 10**-12, 100)
    print(format_table(p_list), end="\n\n")
    print(format_table(empirical_order(p_list), "a_n"), end="\n\n")

    p_list = fixed_point_iteration(g, 0.5, 10**-12, 100)
    print(format_table(p_list), end="\n\n")
    print(format_table(empirical_order(p_list), "a_n"), end="\n\n")
    print(format_table(asymptotic_constant(p_list), "e_n"), end="\n\n")
    print("g' for R_0 = 2.5:", g_prime(p_list[-1]))

    # Basic reproduction number R_0 = 1.3
    n_list = newtons_method(
        lambda x: f(x, R_0=1.3),
        lambda x: f_prime(x, R_0=1.3),
        1,
        10**-12,
        100
    )
    print(format_table(n_list), end="\n\n")
    print(format_table(empirical_order(n_list), "a_n"), end="\n\n")

    n_list = fixed_point_iteration(lambda x: g(x, R_0=1.3), 0.5, 10**-12, 100)
    print(format_table(n_list), end="\n\n")
    print(format_table(empirical_order(n_list), "a_n"), end="\n\n")
    print(format_table(asymptotic_constant(n_list), "e_n"), end="\n\n")
    print("g' for R_0 = 1.3:", g_prime(n_list[-1], R_0=1.3))

    # Basic reproduction number R_0 = 4
    f_list = newtons_method(
        lambda x: f(x, R_0=4),
        lambda x: f_prime(x, R_0=4),
        1,
        10**-12,
        100
    )
    print(format_table(f_list), end="\n\n")
    print(format_table(empirical_order(f_list), "a_n"), end="\n\n")

    f_list = fixed_point_iteration(lambda x: g(x, R_0=4), 0.5, 10**-12, 100)
    print(format_table(f_list), end="\n\n")
    print(format_table(empirical_order(f_list), "a_n"), end="\n\n")
    print(format_table(asymptotic_constant(f_list), "e_n"), end="\n\n")
    print("g' for R_0 = 4:", g_prime(f_list[-1], R_0=4))

    # Basic reproduction number R_0 = 15
    m_list = newtons_method(
        lambda x: f(x, R_0=15),
        lambda x: f_prime(x, R_0=15),
        1,
        10**-12,
        100
    )
    print(format_table(m_list), end="\n\n")
    print(format_table(empirical_order(m_list), "a_n"), end="\n\n")

    m_list = fixed_point_iteration(lambda x: g(x, R_0=15), 0.5, 10**-12, 100)
    print(format_table(m_list), end="\n\n")
    print(format_table(empirical_order(m_list), "a_n"), end="\n\n")
    print(format_table(asymptotic_constant(m_list), "e_n"), end="\n\n")
    print("g' for R_0 = 15:", g_prime(m_list[-1], R_0=15))

    # Test case
    test_list = newtons_method(
        lambda x: f(x, R_0=0.8),
        lambda x: f_prime(x, R_0=0.8),
        1,
        10**-12,
        100
    )
    print(format_table(test_list), end="\n\n")

    # Vaccination study
    for v in [0, 0.3, 0.5, 0.55, 0.59]:
        g_list = newtons_method(
            lambda x: f_vac(x, v),
            lambda x: f_prime_vac(x, v),
            1,
            10**-12,
            100
        )
        print(format_table(g_list), end="\n\n")

    # Sensitivity to initial guess
    for p_0 in [0.3, 0.375, 0.4, 0.5, 0.75, 0.9, 1]:
        print(f"p_0 = {p_0}")
        g_list = newtons_method(f, f_prime, p_0, 10**-12, 100)
        print(format_table(g_list), end="\n\n")


if __name__ == "__main__":
    main()