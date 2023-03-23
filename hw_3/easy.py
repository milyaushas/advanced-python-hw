import os

import numpy as np


class Matrix:
    def __init__(self, data):
        self.n = len(data)
        self.m = len(data[0])
        self.data = data
        for row in data:
            if len(row) != self.m:
                raise ValueError("Invalid matrix")

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Different numbers of rows")
        if self.m != other.m:
            raise ValueError("Different numbers of columns")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.m)] for i in range(self.n)])

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Different numbers of rows")
        if self.m != other.m:
            raise ValueError("Different numbers of columns")
        return Matrix([[self.data[i][j] * other.data[i][j] for j in range(self.m)] for i in range(self.n)])

    def __matmul__(self, other):
        if self.m != other.n:
            raise ValueError("Incompatible sizes")
        result = [[0 for j in range(other.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)


def format_matrix(matrix):
    return "[" + ",\n ".join(str(line) for line in matrix.data) + "]"


def easy():
    np.random.seed(0)
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("./hw_3/artifacts/easy/matrix+.txt", "w") as f:
        f.write(format_matrix(a + b))

    with open("./hw_3/artifacts/easy/matrix*.txt", "w") as f:
        f.write(format_matrix(a * b))

    with open("./hw_3/artifacts/easy/matrix@.txt", "w") as f:
        f.write(format_matrix(a @ b))

print(os.getcwd())
easy()
