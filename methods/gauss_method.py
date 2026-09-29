from tools import copy_matrix, matrix_size


def gauss(
    A: list[list[float]],
    b: list[float],
    eps: float = 1e-10
) -> tuple[list[float], list[list[float]]]:

    A = copy_matrix(A)
    b = b.copy()

    n, m = matrix_size(A)

    for k in range(n - 1):

        # Поиск главного элемента
        pivot = k

        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[pivot][k]):
                pivot = i

        # Проверка главного элемента
        if abs(A[pivot][k]) < eps:
            raise ValueError(
                "Система не имеет единственного решения"
            )

        # Перестановка строк
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            b[k], b[pivot] = b[pivot], b[k]

        # Прямой ход метода Гаусса
        for i in range(k + 1, n):

            factor = A[i][k] / A[k][k]

            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

            b[i] -= factor * b[k]

    # Обратная подстановка
    x = backward_substitution(A, b, eps)

    return x, A


def backward_substitution(
    U: list[list[float]],
    b: list[float],
    eps: float
) -> list[float]:

    n = len(U)

    x = [0.0] * n

    for i in range(n - 1, -1, -1):

        s = 0.0

        for j in range(i + 1, n):
            s += U[i][j] * x[j]

        if abs(U[i][i]) < eps:
            raise ValueError(
                "Нулевой диагональный элемент"
            )

        x[i] = (b[i] - s) / U[i][i]

    return x