#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from scipy import stats
import math

def normal(u=0, s=1):
    def fun(x):
        return stats.distributions.norm.cdf(x, loc=u, scale=s)
    return fun

def gamma(a, l=1):
    def fun(x):
        return stats.distributions.gamma.cdf(x, a, loc=0, scale=l)
    return fun

def normal_drv(u=0, s=1):
    def fun(x):
        return stats.distributions.norm.pdf(x, loc=u, scale=s)
    return fun

def gamma_drv(a, l=1):
    def fun(x):
        return stats.distributions.gamma.pdf(x, a, loc=0, scale=l)
    return fun

def polynomial(*args):
    """Returns a polynomial function with closed coefficients.
    Eg. polynomial(3, 2, 1) = fun(x) returning 3x^2 + 2x + 1
    """
    def fun(x):
        return sum([arg*pow(x, i) for i, arg in enumerate(reversed(args))])
    return fun

def func_a(x):
    """e^(-x) - x"""
    return math.exp(-x) - x

def func_a_drv(x):
    """-e^(-x) - 1"""
    return -math.exp(-x) - 1

def func_b(a):
    """e^(-ax) - x"""
    def fun(x):
        return math.exp(-a*x) - x
    return fun

def func_b_drv(a):
    """-a*e^(-ax) - 1"""
    def fun(x):
        return -a * math.exp(-a*x) - 1
    return fun

def func_c(a):
    """a - sin(1/x)"""
    def fun(x):
        return a - math.sin(1/x)
    return fun

def func_c_drv(a):
    """(cos(1/x))/x^2"""
    def fun(x):
        return math.cos(1/x)/x**2
    return fun
