# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:53:07 2017

@author: Josh
"""
from lecture3_segment3 import *

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
g.edges={}
for n in nodes:
    g.addNode(n)
    
    
for i in nodes:
    for j in nodes:
        name1 = i.getName()
        name2 = j.getName()
        if name1[0:2]==name2[1::-1]:
            if not j in g.childrenOf(i):
                g.addEdge(Edge(i,j))
        elif name1[1:]==name2[2:0:-1]:
            if not j in g.childrenOf(i):
                g.addEdge(Edge(i,j))
            
    print(g)