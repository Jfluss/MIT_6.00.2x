#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:33:25 2017

@author: joshfluss
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    bucket = ['red', 'red', 'red', 'green', 'green', 'green']
    num_same = 0
    for i in range(numTrials):
        new_bucket = bucket[:]
        draw = []
        for i in range(3):
            choice = random.choice(new_bucket)
            draw.append(choice)
            new_bucket.remove(choice)
        if draw[0] == draw[1] and draw[1] == draw[2]:
            num_same+=1
    return float(num_same/numTrials)   
        