# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:19:55 2014

@author: augustin
"""

import sys
if len(sys.argv) < 3:
    print("Error : 2 arguments are expected")
else:
    OP1 = int(sys.argv[1])
    OP2 = int(sys.argv[2])
    print(OP1 + OP2)
