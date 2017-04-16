# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:20:56 2017

@author: Josh
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max = 0
    if len(L) == 1:
        return L[0]
    for i in range(1,len(L)+1):
        if sum(L[0:i]) > max:
            max = sum(L[0:i])
    next_max = max_contig_sum(L[1:])  
    if next_max>max:
        max = next_max
    return max
        