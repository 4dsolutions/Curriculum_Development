#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:57:28 2020

@author: StatsGnewt
"""
import pandas as pd

from math import factorial

def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def sum_binom(n, x):
    return sum(choose(n,k) * x**k for k in range(0, n+1))

def pascal(n):
    return [choose(n,k) for k in range(0,n+1)]

def get_coasters():
    coasters = pd.read_csv("./data/roller_coasters.csv")
    return coasters

def z_score(x, mu, sigma, n=1):
    return (x - mu)/(sigma/math.sqrt(n))
