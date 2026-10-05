from pathlib import Path

from tools import (
    matrix_to_latex,
    vector_to_latex,
    latex_table,
)


RESULTS_DIR = Path("results")


def save_text(
        filename: str,
        content: str
) -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    path = RESULTS_DIR / filename
    path.write_text(content, encoding="utf-8")


def save_gaussian_results(
        U: list[list[float]],
        x: list[float],
        residual_norm: float,
) -> None:
    content = (
        "\\section*{Метод Гаусса}\n\n"
        "Полученная верхнетреугольная матрица:\n\n"
        "\\[\n"
        f"{matrix_to_latex(U)}\n"
        "\\]\n\n"
        "Решение системы:\n\n"
        "\\[\n"
        f"x = {vector_to_latex(x)}\n"
        "\\]\n\n"
        f"Норма невязки: ${residual_norm:.6e}$\n"
    )

    save_text("gaussian.tex", content)


def save_lu_results(
        L: list[list[float]],
        U: list[list[float]],
        x: list[float],
        residual_norm: float,
) -> None:
    content = (
        "\\section*{LU-разложение}\n\n"
        "Матрица $L$:\n\n"
        "\\[\n"
        f"{matrix_to_latex(L)}\n"
        "\\]\n\n"
        "Матрица $U$:\n\n"
        "\\[\n"
        f"{matrix_to_latex(U)}\n"
        "\\]\n\n"
        "Решение системы:\n\n"
        "\\[\n"
        f"x = {vector_to_latex(x)}\n"
        "\\]\n\n"
        f"Норма невязки: ${residual_norm:.6e}$\n"
    )

    save_text("lu.tex", content)


def save_comparison_table(
        rows: list[list[str]],
) -> None:
    headers = [
        "Метод",
        "Число итераций",
        "Норма невязки",
        "Норма ошибки",
    ]

    table = latex_table(
        headers=headers,
        rows=rows,
        caption="Сравнение численных методов решения СЛАУ",
    )

    save_text("comparison_table.tex", table)

def save_solution_table(
        solutions: list[tuple[str, list[float]]],
) -> None:
    columns = len(solutions[0][1])

    headers = ["Метод"] + [
        f"$x_{{{i}}}$"
        for i in range(1, columns + 1)
    ]

    rows = []

    for method, solution in solutions:
        row = [method] + [
            f"{value:.6f}"
            for value in solution
        ]
        rows.append(row)

    table = latex_table(
        headers=headers,
        rows=rows,
        caption="Таблица результатов вычислений",
    )

    save_text("solution_table.tex", table)