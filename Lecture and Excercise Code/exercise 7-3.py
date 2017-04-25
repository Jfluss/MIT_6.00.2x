#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:26:36 2017

@author: joshfluss
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    else:
        l=[]
        for i in L:
          l.append(len(i))  
        m=0
        for i in l:
           m+=i
        mean = m/len(l)
        v=0
        for i in l:
            v+=(i-mean)**2
        var = v/len(l)
        sd = (var)**.5   
    return sd