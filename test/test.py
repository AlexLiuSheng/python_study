# coding=utf-8
'python study '
from test import module

__author__ = 'Allen Liu'
import functools
import os
import sys
from functools import reduce

from typing import List

print(sys.version)
print('%2d %%' % 0o2)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


# 可变参数
def variableParams(*numbers):
    print(numbers)
    return None


# 关键字参数
def keyParams(age, name, **numbers):
    print('age:', age, 'name:', name, 'others:', numbers)
    return None


# 命名关键字参数
def defineKeyParams(age, name, *, city="chengdu", job):
    print(job)
    return None


variableParams(1, 2, 3)
keyParams(18, 'hehe', city="")
defineKeyParams(18, 'name', job='it')
# 切片
l = ['a', 'b', 'c', 'd', 'e']
print(l[:3])
print(l[-3:])
print(l[:3:2])
print(l[::3])
print(l[-3::2])

for i in l:
    print(i)

print(isinstance(l, List))

# index for
for i, value in enumerate(l):
    print("index:", i, "value", value)

# range for
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 列表生成式
L2 = [x * x for x in range(1, 11)]

print([x + y for x in 'ABC' for y in 'XYZ' if x == 'A'])

print([f for f in os.listdir('.')])


# yield 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        a, b, n = b, a + b, n + 1
    return 'done'


f = fib(6)
for i in range(6):
    print(next(f))


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-3, 4, abs))


# map 变换
def f(x):
    return x * x


r = map(f, [1, 2, 3])
print(list(r))


# reduce 把结果继续和下一个元素做累积
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7]))

# str to int
Unit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int():
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return Unit[s]

    # return reduce(fn, map(char2num, '13579'))
    return reduce(lambda x, y: x * 10 + y, map(lambda x: Unit[x], '13237'))


print(str2int())


# filer

def test(x):
    return x % 2 == 1


print(list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9])))
print(list(filter(lambda x: x is not None, ['a', 'b', None, 'c', 'None'])))

# sorted
print(sorted([1, -3, -5, 4, 6], key=lambda x: x * x))


# 函数返回值
def lazy_sum(a):
    def sum():
        return a * a

    return sum


print(lazy_sum(2))


# 闭包 ：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 装饰器：假设我们要增强now()函数的功能，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kwargs):
        print('call', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now(a):
    print(a)
    print("2018-11-21")


# 偏函数
max2 = functools.partial(max, 10)
print(max2(*(5, 6, 7)))

module.test()
