#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:56:06 2017

@author: joshfluss
"""

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    results=[]
    for i in range(numTrials):
        rolls = []
        best = 1
        run = 1
        for j in range(numRolls):
            rolls.append(die.roll())
            if j>0 and rolls[j]==rolls[j-1]:
                run += 1
                if run>best:
                    best = run
            else:
                run = 1
        results.append(best)
    makeHistogram(results, 10, 'Longest Run', '# of Counts')
    return getMeanAndStd(results)[0]