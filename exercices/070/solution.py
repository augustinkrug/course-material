# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:07:05 2014

@author: augustin
"""

for i in range(ord('a'), ord('z')+1):
    for j in range(ord('a'), ord('z')+1):
        if i != j:
            print(chr(i) + chr(j))
        else:
            continue
