import numpy as np
from easy import Matrix, format_matrix
from medium import MatrixWithMixins
from hard import HashableMatrix, clear_cache


def easy():
    np.random.seed(0)
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("artifacts/easy/matrix+.txt", "w") as f:
        f.write(format_matrix(a + b))

    with open("artifacts/easy/matrix*.txt", "w") as f:
        f.write(format_matrix(a * b))

    with open("artifacts/easy/matrix@.txt", "w") as f:
        f.write(format_matrix(a @ b))


def medium():
    np.random.seed(0)
    a = MatrixWithMixins(np.random.randint(0, 10, (10, 10)))
    b = MatrixWithMixins(np.random.randint(0, 10, (10, 10)))

    sum = a + b
    sum.write_to_file("artifacts/medium/matrix+.txt")

    mul = a * b
    mul.write_to_file("artifacts/medium/matrix*.txt")

    matmul = a @ b
    matmul.write_to_file("artifacts/medium/matrix@.txt")


def hard():
    A = HashableMatrix([[0, 1], [2, 3]])
    C = HashableMatrix([[777, 13169], [42, 3]])
    assert A.__hash__() == C.__hash__()

    B = HashableMatrix([[4, 5], [6, 7]])
    D = HashableMatrix([[4, 5], [6, 7]])

    A.write_to_file("artifacts/hard/A.txt")
    B.write_to_file("artifacts/hard/B.txt")
    C.write_to_file("artifacts/hard/C.txt")
    D.write_to_file("artifacts/hard/D.txt")

    AB = A @ B
    clear_cache()
    CD = C @ D
    AB.write_to_file("artifacts/hard/AB.txt")
    CD.write_to_file("artifacts/hard/CD.txt")

    with open("artifacts/hard/hash.txt", "w") as file:
        file.write("Hash of AB: ")
        file.write(str(AB.__hash__()))
        file.write("\nHash of CD: ")
        file.write(str(CD.__hash__()))


def main():
    easy()
    medium()
    hard()


if __name__ == "__main__":
    main()
