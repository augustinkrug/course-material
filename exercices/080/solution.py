# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:07:05 2014

@author: augustin
"""
debut = ord('a')-1
for i in range(ord('a'), ord('z')+1):
    debut = debut + 1
    for j in range(debut, ord('z')+1):
        print(chr(i) + chr(j))
