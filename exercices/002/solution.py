# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 09:44:27 2014

@author: augustin
"""
text = ''
vowels = {'a', 'e', 'i', 'o', 'u'}
for i in range(ord('a'), ord('z')+1):
    if chr(i) in vowels:
        c = i-32
    else:
        c = i
    text = chr(c) + text
print(text)
