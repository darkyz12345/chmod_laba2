def matrix_to_latex(
        A: list[list[float]],
        precision: int = 6
) -> str:
    """Преобразует матрицу в LaTeX."""

    rows = []

    for row in A:
        values = [f"{value:.{precision}g}" for value in row]
        rows.append(" & ".join(values))

    return (
        "\\begin{pmatrix}\n"
        + " \\\\\n".join(rows)
        + "\n\\end{pmatrix}"
    )


def vector_to_latex(
        vector: list[float],
        precision: int = 6
) -> str:
    """Преобразует вектор в LaTeX."""

    values = [f"{value:.{precision}g}" for value in vector]

    return (
        "\\begin{pmatrix}\n"
        + " \\\\\n".join(values)
        + "\n\\end{pmatrix}"
    )


def latex_table(
        headers: list[str],
        rows: list[list[str]],
        caption: str = ""
) -> str:
    """Создаёт таблицу в формате LaTeX."""

    columns = len(headers)
    column_format = "|" + "c|" * columns

    result = [
        "\\begin{table}[H]",
        "\\centering",
    ]

    if caption:
        result.append(f"\\caption{{{caption}}}")

    result.extend([
        f"\\begin{{tabular}}{{{column_format}}}",
        "\\hline",
        " & ".join(headers) + " \\\\",
        "\\hline",
    ])

    for row in rows:
        result.append(" & ".join(row) + " \\\\")

    result.extend([
        "\\hline",
        "\\end{tabular}",
        "\\end{table}",
    ])

    return "\n".join(result)