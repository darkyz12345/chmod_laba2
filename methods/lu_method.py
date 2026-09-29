from tools import matrix_size, copy_matrix
from .gauss_method import backward_substitution

def lu_decomposition(
        A: list[list[float]],
        eps: float = 1e-10
) -> tuple[list[list[float]], list[list[float]]]:
    n, m = matrix_size(A)
    if n != m:
        raise ValueError("Для LU-разложения матрица должна быть квадратной")
    A = copy_matrix(A)
    L = [
        [0.0 for _ in range(n)]
        for _ in range(n)
    ]
    U = [
            [0.0 for _ in range(n)]
            for _ in range(n)
        ]
    for i in range(n):
        L[i][i] = 1.0
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(i):
                s += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - s
        if abs(U[i][i]) < eps:
            raise ValueError("LU-разложение невохможно (нудевой диагональный элемент)")
        for j in range(i + 1, n):
            s = 0.0
            for k in range(i):
                s += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - s) / U[i][i]
    return L, U

def forward_substitution(
        L: list[list[float]],
        b: list[float],
        eps: float = 1e-10
) -> list[float]:
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(i):
            s += L[i][j] * y[j]
        if abs(L[i][i]) < eps:
            raise ValueError("Нулевой диагональный элемент")
        y[i] = (b[i] - s) / L[i][i]
    return y

def lu_solve(
        A: list[list[float]],
        b: list[float],
        eps: float = 1e-10
) -> tuple[
    list[float],
    list[list[float]],
    list[list[float]],
    list[float]
]:
    L, U = lu_decomposition(A, eps)
    y = forward_substitution(L, b, eps)
    x = backward_substitution(U, y, eps)
    return x, L, U, y