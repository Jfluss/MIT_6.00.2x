#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:11:28 2017

@author: joshfluss
"""
import numpy as np
from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    if len(choices) == 1:
        if choices[0] < total:
            return np.array([1])
        else:
            return np.array([0])
    add = 0
    results = []
    for i in powerset(choices):
        if sum(i) == total:
            answer = []
            for j in choices:
                if j in i:
                    answer.append(1)
                else:
                    answer.append(0)
            return np.array(answer)
    for i in choices:
        if (add + i) <= total:
            add += i
            results.append(1)
        else:
            results.append(0)
        guess = np.array(results)
    if add != total:
        results = np.array([0])
        results = np.append(results, find_combination(choices[1:], total))
    if total-(results*np.array(choices)).sum() < total-(guess*np.array(choices)).sum():
        guess = results[:]
    return guess

