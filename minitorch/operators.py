"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(a, b):
    return a * b

def id(a):
    return a

def add(a, b):
    return a + b

def neg(a):
    return -1.0 * a

def lt(a, b):
    if a < b:
        return 1.0
    return 0.0

def eq(a, b):
    if a == b:
        return 1.0
    return 0.0

def max(a, b):
    if a <= b:
        return b
    return a

def is_close(a, b):
    return abs(a - b) < 1e-2

def sigmoid(a):
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    return math.exp(a) / (1 + math.exp(a))

def relu(a):
    if a <= 0:
        return 0.0
    return a

def log(a):
    return math.log(a)

def exp(a):
    return math.exp(a)

def log_back(a, b):
    return b / a

def inv(a):
    return a ** -1

def inv_back(a, b):
    return -b / a ** 2

def relu_back(a, b):
    if a <= 0:
        return 0.0
    return b

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(f):
    def _map(a):
        return [f(i) for i in a]
    return _map

def zipWith(f):
    def _zipWith(a, b):
        return [f(i, j) for i, j in zip(a, b)]
    return _zipWith

def reduce(f, s):
    def _reduce(a):
        res = s
        for i in a:
            res = f(res, i)
        return res
    return _reduce

def negList(a):
    return map(neg)(a)

def addLists(a, b):
    return zipWith(add)(a, b)

def sum(a):
    return reduce(add, 0)(a)

def prod(a):
    return reduce(mul, 1)(a)
