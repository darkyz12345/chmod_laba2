from methods import gauss, lu_solve, jacobi
from tools import residual, norma_vector

from results import (
    save_gaussian_results,
    save_lu_results,
    save_comparison_table,
    save_solution_table,
)

from plot import plot_jacobi_convergence


if __name__ == "__main__":
    A = [
        [11.0, 2.0, -2.0, -2.0],
        [2.0, 16.0, -3.0, -2.0],
        [1.0, 4.0, 14.0, -2.0],
        [-2.0, -3.0, -2.0, 13.0],
    ]

    b = [-38.0, -65.0, 24.0, 33.0]

    x_exact = [-2.0, -3.0, 3.0, 2.0]

    eps = 1e-10

    x_gauss, U_gauss = gauss(A, b)

    r_gauss = residual(A, x_gauss, b)
    r_gauss_norm = norma_vector(r_gauss)

    error_gauss = norma_vector([
        x_gauss[i] - x_exact[i]
        for i in range(len(x_exact))
    ])

    save_gaussian_results(
        U_gauss,
        x_gauss,
        r_gauss_norm,
    )

    print("Gauss:")
    print("x =", x_gauss)
    print("r =", r_gauss)
    print("||r|| =", r_gauss_norm)
    print("||x - x*|| =", error_gauss)

    x_lu, L, U, y = lu_solve(A, b)

    r_lu = residual(A, x_lu, b)
    r_lu_norm = norma_vector(r_lu)

    error_lu = norma_vector([
        x_lu[i] - x_exact[i]
        for i in range(len(x_exact))
    ])

    save_lu_results(
        L,
        U,
        x_lu,
        r_lu_norm,
    )

    print("\nLU:")
    print("x =", x_lu)
    print("y =", y)
    print("r =", r_lu)
    print("||r|| =", r_lu_norm)
    print("||x - x*|| =", error_lu)

    x_jacobi, iterations, history = jacobi(
        A,
        b,
        [0.0] * len(b),
        eps,
    )

    plot_jacobi_convergence(history)

    r_jacobi = residual(A, x_jacobi, b)
    r_jacobi_norm = norma_vector(r_jacobi)

    error_jacobi = norma_vector([
        x_jacobi[i] - x_exact[i]
        for i in range(len(x_exact))
    ])

    solutions = [
        ("Метод Гаусса", x_gauss),
        ("LU-факторизация", x_lu),
        ("Метод Якоби", x_jacobi),
    ]

    save_solution_table(solutions)

    print("\nJacobi:")
    print("x =", x_jacobi)
    print("iterations =", iterations)
    print("r =", r_jacobi)
    print("||r|| =", r_jacobi_norm)
    print("||x - x*|| =", error_jacobi)

    rows = [
        [
            "Гаусс",
            "---",
            f"${r_gauss_norm:.6e}$",
            f"${error_gauss:.6e}$",
        ],
        [
            "LU",
            "---",
            f"${r_lu_norm:.6e}$",
            f"${error_lu:.6e}$",
        ],
        [
            "Якоби",
            str(iterations),
            f"${r_jacobi_norm:.6e}$",
            f"${error_jacobi:.6e}$",
        ],
    ]

    save_comparison_table(rows)