#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:11:21 2017

@author: joshfluss
"""


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        combo = (bag1, bag2)
        for j in range(N):
            # test bit jth of integer i
            print(i, j)
            if (i // 3**j) % 3 == 1:   
                bag1.append(items[j])
            if (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield combo