# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:28:47 2014

@author: augustin
"""

station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}
titles = list(station.keys())
for i in range(len(titles)):
    print(titles[i], station[titles[i]])
