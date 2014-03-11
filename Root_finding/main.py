#!/usr/bin/python
# -*- coding: utf-8 -*-
from functions import *
import math

def samesign(a, b):
    return a*b > 0

def bisect(func, a, b, val=0, eps=1e-10):
    """For given function func and interval [a, b] returns c
    with accuracy >= eps such that f(c) = val"""
    a, b = min(a, b), max(a, b)
    fun_a = func(a) - val
    assert not samesign(fun_a, func(b) - val)
    """Calculating number of iterations from formula"""
    ln = math.log
    num_iters = int(math.ceil((ln(b-a) - ln(eps))/ln(2)))
    for i in xrange(num_iters):
        c = (a + b)/2.
        fun_c = func(c) - val
        if samesign(fun_a, fun_c):
            a = c
            fun_a = fun_c
        else:
            b = c
    return (a + b)/2.

def newton(func, func_drv, c, val=0, eps=1e-10, dt=1e-6, num_iters=100):
    """For given function func, its drvative func_drv and
    starting point c returns c with accuracy >= eps such that f(c) = val
    returns c prematurely if fun(c) stops converging."""
    fun_c = func(c) - val
    delta_c = dt + 1
    for i in xrange(num_iters):
        if abs(fun_c) > eps or delta_c > dt:
            delta_c = fun_c/func_drv(c)
            c = c - delta_c
            fun_c = func(c) - val
        else:
            return c
    return c

def secant(func, a, b, val=0, eps=1e-6, num_iters=100):
    a, b = min(a, b), max(a, b)
    fun_a, fun_b = func(a), func(b)
    c = b - fun_b*(b - a)/(fun_b - fun_a)
    for i in xrange(num_iters):
        if abs(func(c) - val) > eps:
            a, b = b, c
            fun_a, fun_b = func(a), func(b)
            c = b - fun_b*(b - a)/(fun_b - fun_a)
    return c

if __name__ == '__main__':
    print 'Running all methods on example function e^(-x) - x...'
    print 'Bisection method: %.9f' % bisect(func_a, a=-2, b=4)
    print 'Newton method: %.9f' % newton(func_a, func_a_drv, c=0)
    print 'Secant method: %.9f' % secant(func_a, a=-2, b=4)
