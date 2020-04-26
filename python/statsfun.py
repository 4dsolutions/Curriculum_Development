#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:57:28 2020

@author: StatsGnewt

Using some support for type hints
https://docs.python.org/3/library/typing.html
"""

from typing import Sequence
import pandas as pd
from itertools import product
from math import factorial, sqrt
from random import shuffle

def deck_of_cards(shuffled = True):
    face_cards = ['Ace', 'King', 'Queen', 'Jack']
    numb_cards = [str(i) for i in range(2, 11)]
    suits      = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    # match every card with every suit
    cards = list(product(face_cards + numb_cards, suits)) 
    if shuffled:
        shuffle(cards)
    return cards

def mean(iterable : Sequence) -> float:
    return sum(iterable)/len(iterable)

def var(iterable : Sequence) -> float:
    av = mean(iterable)
    return sum([(x - av)**2 for x in iterable])/len(iterable)

def std(iterable : Sequence) -> float:
    return sqrt(var(iterable))
    
def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def sum_binom(n, x):
    return sum(choose(n,k) * x**k for k in range(0, n+1))

def pascal(n):
    return [choose(n,k) for k in range(0,n+1)]

def pascal_gen():
    row = [1]
    while True:
        yield row
        row = [i+j for i, j in zip(row + [0], [0] + row)]
    
def get_coasters():
    coasters = pd.read_csv("./data/roller_coasters.csv")
    return coasters

def z_score(x, mu, sigma, n=1):
    return (x - mu)/(sigma/sqrt(n))

