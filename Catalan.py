# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:52:06 2019
Program for nth Catalan Number
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. 
For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
2) Count the number of possible Binary Search Trees with n keys
3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
"""

def catalan(n):
    if n<=1:
        return 1;
    total=0
    for i in range(n):
        total=total+catalan(i)*catalan(n-1-i)
    return total