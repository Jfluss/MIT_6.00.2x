#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:24:33 2017

@author: joshfluss
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    
    import random
    basket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
    success = 0
    for i in range(numTrials):
        choices = []
        choices = random.sample(basket, 3)
        if choices[0]==choices[1] and choices[1]==choices[2]:
            success += 1
    ans = float(success/numTrials)
    return ans