from easy import Matrix
from medium import PrettyViewMixin, WriteToFileMixin


class HashMixin:
    # сумма всех элементов a_ij матрицы, возведенных в i степень и умноженных на j, по модулю большого простого числа
    def __hash__(self):
        hash_ = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                hash_ += (self.data[i][j]) ** i * j
        return hash_ % 900900900900990990990991


def clear_cache():
    HashableMatrix._matmul_cache.clear()


class HashableMatrix(Matrix, HashMixin, PrettyViewMixin, WriteToFileMixin):
    _matmul_cache = {}

    def __matmul__(self, other):
        if self.n != other.n:
            raise ValueError("Different numbers of rows")
        if self.m != other.m:
            raise ValueError("Different numbers of columns")

        key = (self.__hash__(), other.__hash__())
        if key not in HashableMatrix._matmul_cache:
            HashableMatrix._matmul_cache[key] = HashableMatrix(super().__matmul__(other).data)
        return HashableMatrix._matmul_cache[key]

