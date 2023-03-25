import numpy as np
import numbers


class WriteToFileMixin:
    def write_to_file(self, filepath):
        with open(filepath, "w") as file:
            file.write(self.__str__())


class PrettyViewMixin:
    def __str__(self):
        return "[" + ",\n ".join(str(line) for line in self.data) + "]"


class DataManagerMixin:
    def __init__(self, data):
        self.__data = np.asarray(data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class MatrixWithMixins(np.lib.mixins.NDArrayOperatorsMixin, DataManagerMixin, PrettyViewMixin, WriteToFileMixin):
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MatrixWithMixins,)):
                return NotImplemented

        inputs = tuple(x.data if isinstance(x, MatrixWithMixins) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, MatrixWithMixins) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
