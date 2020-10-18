"""
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__} run time: {time.time() - start}")
        return ret
    return inner


@timer
def f1():
    print("Hello world")


@timer
def f2(*args):
    return sum(args)


@timer
def f3(m: int, n: int):
    for _ in range(m):
        for _ in range(n):
            pass


@timer
def f4(n):
    return sum(range(n))


if __name__ == "__main__":
    f1()
    print(f"the sum is {f2(1, 2, 3)}")
    f3(10000, 10000)
    print(f"the sum of {0} to {1234567 - 1} is {f4(1234567)}")
