# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:55:18 2014

@author: augustin
"""
even = 0
for i in range(1, 100 + 1):
    if divmod(i, 2)[1] == 0:
        print(i)
