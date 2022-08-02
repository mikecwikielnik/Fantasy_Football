"""
2022 Fantasy Football Weighted Lottery 
"""

import random 
import pprint

sampleList = ['mike', 'elwell', 'brown',
              'oc', 's longo', 'hermanson']
randomList = random.choices(
  sampleList, weights=(12.125, 10.75, 10, 3, 10, 6.25), k=10)
  
pprint.pprint(randomList)

# The model below is probably the model you are going to go with. 
# We need to figure out whether or not if we can creep past two decimal places 

import numpy as np

numpyList = np.random.choice(sampleList, size=6, replace=False, p=(0.16, 0.16, 0.16, 0.16, 0.16, 0.20))

print(numpyList)