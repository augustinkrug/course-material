# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:19:58 2014

@author: augustin
"""

import sys
name = sys.argv[0]

for i in range(len(name)):
    if name[-i-1] == "/":
        print(name[-i:])
        break
    else:
        continue
