#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:14:39 2017

@author: joshfluss
"""

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
#    even = []
#    for i in range(0,100,2):
#        even.append(i)
#    while True:
#        ans = random.randint(0,100)
#        if ans in even:
#            return ans
#        else:
#            continue
    return random.randrange(0,100,2)
    