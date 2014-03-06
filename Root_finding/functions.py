#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import math


def polynomial(*args):
    """Returns a polynomial function with closed coefficients.
    Eg. polynomial(3, 2, 1) = 3x^2 + 2x + 1
    """
    def fun(x):
        return sum([arg*pow(x, i) for i, arg in enumerate(reversed(args))])
    return fun

def function_a(x):
    """e^(-x) - x"""
    return math.exp(-x) - x

def function_a_deriv(x):
    """-e^(-x) - 1"""
    return -math.exp(-x) - 1

def function_b(a):
    """e^(-ax) - x"""
    def fun(x):
        return math.exp(-a*x) - x
    return fun

def function_b_deriv(a):
    """-a*e^(-ax) - 1"""
    def fun(x):
        return -a * math.exp(-a*x) - 1
    return fun

def function_c(a):
    """a - sin(1/x)"""
    def fun(x):
        return a - math.sin(1/x)
    return fun

def function_c_deriv(a):
    """(cos(1/x))/x^2"""
    def fun(x):
        return math.cos(1/x)/x**2
    return fun
