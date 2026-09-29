def copy_matrix(A: list[list[float]]) -> list[list[float]]:
    """Copy matrix

    Args:
        A (list[list[float]]): matrix

    Returns:
        list[list[float]]: matrix
    """
    return [
        [r for r in row] for row in A
    ]

def matrix_size(A: list[list[float]]) -> tuple[int, int]:
    """Size of matrix

    Args:
        A (list[list[float]]): matrix

    Returns:
        tuple[int, int]: size of matrix
    """
    return len(A), len(A[0])


def augmented_matrix(A: list[list[float]], b: list[float]) -> list[list[float]]:
    """Augmented matrix

    Args:
        A (list[list[float]]): matrix A
        b (list[float]): col b

    Returns:
        list[list[float]]: augmented matrix A|b
    """
    return [
        [r for r in A[i]] + [b[i]]
        for i in range(len(A))
    ]


def determinant(A: list[list[float]]) -> float:
    size = matrix_size(A)
    if size[0] != size[1]:
        raise ValueError("Для нахожжения определителя матрицы матрица должна быть квдратной")
    n = size[0]
    A = copy_matrix(A)
    det = 1.0
    for k in range(n):
        pivot = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[pivot][k]):
                pivot = i
        if abs(A[pivot][k]) < 1e-10:
            return 0.0
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            det *= -1
        pivot_value = A[k][k]
        det *= pivot_value
        for i in range(k + 1, n):
            factor = A[i][k] / pivot_value
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
    return det

def matrix_multiply(
        A: list[list[float]],
        B: list[list[float]]
) -> list[list[float]]:
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    result = [
        [0.0 for _ in range(p)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrices_close(
        A: list[list[float]],
        B: list[list[float]],
        eps: float = 1e-10
) -> bool:
    n, m = matrix_size(A)
    if matrix_size(B) != (n, m):
        return False
    for i in range(n):
        for j in range(m):
            if abs(A[i][j] - B[i][j]) > eps:
                return False
    return True