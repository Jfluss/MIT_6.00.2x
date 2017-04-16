# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:33:37 2017

@author: Josh
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    answer = []
    if L ==[]:
        pass
    else:
        s_copy = s
        for i in range(len(L[:-1])):
            n=0
            while s_copy > L[i+1]:
                if s_copy >= L[i]:
                    n+=1
                    s_copy-=L[i]
                else:
                    break
            answer.append(n)
    #        print(n)
    #        print(s_copy)
        if s_copy%L[-1] > 0:
            return 'no solution'
        else:
            m=0
            while s_copy>=L[-1]:
                m+=1
                s_copy-=L[-1]
    #            print(m)
    #            print(s_copy)
            answer.append(m)
    #    for i in range(len(answer[1:])):
    #        if answer[i+1] > answer[i]:
    #            return 'no solution'
    #    print(answer)
    if sum(answer)==0:
        return 'no solution'
    else:
        return sum(answer)
        
    