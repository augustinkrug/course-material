# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:55:18 2014

@author: augustin
"""
total = 0
for i in range(1, 1000):
    if divmod(i, 3)[1] == 0 or divmod(i, 5)[1] == 0:
        total = total + i
print(total)
