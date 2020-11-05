"""
自定义一个 python 函数，实现 map() 函数的功能。
"""

from typing import Callable, Iterable, Iterator


def my_map(func: Callable, *iterables: Iterable) -> Iterator:
    for i in zip(*iterables):
        yield func(*i)
    # return (func(*i) for i in zip(*iterables))


def square(x):
    return x * x


if __name__ == "__main__":
    # one iterable args
    py_a = map(square, range(5))
    my_a = my_map(square, range(5))
    for i in range(5):
        assert next(py_a) == next(my_a)

    # multiple iterable args and different length
    py_b = map(lambda x, y: x + y, range(5), range(10, 20))
    my_b = my_map(lambda x, y: x + y, range(5), range(10, 20))
    for n in py_b:
        assert n == next(my_b)

    py_c = map(lambda x, y: x * y, [1, 2, 3, 4], {4, 3, 2, 1})
    my_c = my_map(lambda x, y: x * y, [1, 2, 3, 4], {4, 3, 2, 1})
    assert list(py_c) == list(my_c)
