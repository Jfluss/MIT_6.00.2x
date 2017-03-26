# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:07:56 2017

@author: Josh
"""

from lecture3_segment3 import *

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight=weight
        pass
    def getWeight(self):
        return self.weight
        pass
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.weight) + ')'
        pass