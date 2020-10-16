#!/usr/bin/python
# -*- coding: utf-8 -*-

from mymath.sequences import recursive
from mymath.sequences.recursive import fib
from mymath.consts import PI
import timeit

print(recursive.fib(3))
print(fib(3))
print(PI)

t_fib = timeit.timeit('fib(100)', number=10000, setup="from mymath.sequences.recursive import fib")
t_fib_gen = timeit.timeit('fib_gen(100)', number=10000, setup="from mymath.sequences.recursive import fib_gen")
print('fib:     {0:.4f}'.format(t_fib))
print('fib_gen: {0:.4f}'.format(t_fib_gen))
