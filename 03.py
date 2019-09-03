# -*- encoding: utf-8 -*-
"""
@File    : 03.py
@Time    : 2019/8/28 9:16
@Author  : HeKai
@Email   : hek@corp.21cn.com
@Software: PyCharm
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
