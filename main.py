from methods import gauss


if __name__ == "__main__":
    A = [
    [2.0, 1.0, 1.0],
    [1.0, 3.0, 2.0],
    [1.0, 2.0, 3.0],
    ]

    b = [6.0, 10.0, 11.0]

    x, U = gauss(A, b)

    print("x =", x)

    print("\nU =")
    for row in U:
        print(row)