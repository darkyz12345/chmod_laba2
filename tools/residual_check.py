def matrix_vector_multiply(
        A: list[list[float]],
        x: list[float]
) -> list[float]:
    res = []
    for row in A:
        value = 0.0
        for j in range(len(x)):
            value += row[j] * x[j]
        res.append(value)
    return res


def residual(
        A: list[list[float]],
        x: list[float],
        b: list[float]
) -> list[float]:
    Ax = matrix_vector_multiply(A, x)
    return [
        b[i] - Ax[i]
        for i in range(len(b))
    ]