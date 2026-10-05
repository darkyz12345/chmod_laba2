from tools import matrix_size, minus_vector, norma_vector, residual


def jacobi(
        A: list[list[float]],
        b: list[float],
        x_0: list[float],
        eps: float = 1e-10
) -> tuple[list[float], int, list[float]]:
        n, m = matrix_size(A)
        if n != m:
                raise ValueError("Матрица передаваемая должна быть квадратной")
        if len(b) != n:
                raise ValueError("Размерность вектора b не совпадает с размерностью матрицы")
        if len(x_0) != n:
                raise ValueError("Размерность вектора начального приближения x_0 не совпадает с размерностью матрицы")
        for i in range(n):
                if abs(A[i][i]) < sum(map(abs, A[i])) - abs(A[i][i]):
                        raise ValueError("Нет диагонального преобладания")
                if abs(A[i][i]) < eps:
                        raise ValueError("Нулевой диагональный элемент матрицы")
        error = float("inf")
        x_new = [0.0 for _ in range(n)]
        x = [i for i in x_0]
        hist = []
        iterations = 0
        while error > eps:
                x_new = [0.0 for _ in range(n)]
                for i in range(n):
                        s = 0
                        for j in range(n):
                                if i != j:
                                        s += A[i][j] * x[j]
                        x_new[i] = (b[i] - s) / A[i][i]
                error = norma_vector(minus_vector(x_new, x))
                hist.append(norma_vector(residual(A, x_new, b)))
                x = x_new
                iterations += 1
        return x, iterations, hist
