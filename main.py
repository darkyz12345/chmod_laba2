from methods import gauss, lu_solve
from tools import residual, matrix_multiply, matrices_close


if __name__ == "__main__":
    A = [
    [11.0, 2.0, -2.0, -2.0],
    [2.0, 16.0, -3.0, -2.0],
    [1.0, 4.0, 14.0, -2.0],
    [-2.0, -3.0, -2.0, 13.0]
    ]

    b = [-38.0, -65.0, 24.0, 33.0]

    x, U = gauss(A, b)

    print("x =", x)

    print("\nU =")
    for row in U:
        print(row)

    r = residual(A, x, b)
    print(F"Gauss {r=}")
    x_lu, L, U, y = lu_solve(A, b)
    print(f"{y=}")
    print(f"{x_lu}")
    print(f"LU r: {residual(A, x_lu, b)}")

