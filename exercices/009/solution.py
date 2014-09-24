# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 15:08:39 2014

@author: augustin
"""

phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
 taxation of trade routes to outlying star systems is in\
 dispute. Hoping to resolve the matter with a blockade of deadly\
 battleships, the greedy Trade Federation has stopped all shipping to\
 the small planet of Naboo. While the congress of the Republic\
 endlessly debates this alarming chain of events, the Supreme\
 Chancellor has secretly dispatched two Jedi Knights, the guardians of\
 peace and justice in the galaxy, to settle the conflict"""
nb = 0
mot = 0
for i in range(len(phantom_menace)):
    if phantom_menace[i] != " " and mot == 0:
        mot = 1
        nb = nb + 1
    elif phantom_menace[i] != " " and mot == 1:
        continue
    elif phantom_menace[i] == " " and mot == 1:
        mot = 0
    elif phantom_menace[i] == " " and mot == 0:
        continue
print(nb)
