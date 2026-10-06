import matplotlib.pyplot as plt


def plot_jacobi_convergence(
        history: list[float],
        filename: str = 'results/jacobi_convergence.png',
) -> None:
    iterations = list(range(1, len(history) + 1))
    plt.figure(figsize=(8, 5))
    plt.semilogy(
        iterations,
        history,
        marker='o',
        markersize=4
    )
    plt.xlabel("Номер итерации $k$")
    plt.ylabel(r"$\|r^{(k)}\|_2$")
    plt.title("Сходимость метода Якоби")
    plt.grid(True, which='both')
    plt.tight_layout()
    plt.savefig(filename, dpi=500, bbox_inches="tight")
    plt.close()