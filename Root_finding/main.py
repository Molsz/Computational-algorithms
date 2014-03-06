#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from functions import *
import math

def samesign(a, b):
    return a*b > 0

def bisect(fun, a, b, eps=1e-6):
    a, b = min(a, b), max(a, b)
    ln = math.log
    num_iters = int(math.ceil((ln(b-a) - ln(eps))/ln(2)))
    for i in xrange(num_iters):
        c = (a + b)/2
        if samesign(fun(a), fun(c)):
            a = c
        else:
            b = c
    return c

def tangent(fun, fun_deriv, x, eps=1e-6):
    c = x
    while abs(fun(c)) > eps:
        c = c - fun(c)/fun_deriv(c)
    return c

def secant(fun, a, b, eps=1e-6):
    a, b = min(a, b), max(a, b)
    c = b - fun(b)*(b - a)/(fun(b) - fun(a))
    while abs(fun(c)) > eps:
        a, b = b, c
        c = b - fun(b)*(b - a)/(fun(b) - fun(a))
    return c

if __name__ == '__main__':
    print 'Running all methods on example function e^(-x) - x...'
    print 'Bisection method: %.9f' % bisect(func_a, a=-2, b=4)
    print 'Newton method: %.9f' % tangent(func_a, func_a_deriv, x=0)
    print 'Secant method: %.9f' % secant(func_a, a=-2, b=4)
