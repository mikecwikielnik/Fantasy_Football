"""
To generate random values to represent fantasy football draft positions. 

"""

#   Random Integer Values

from random import randint
from statistics import mean
from statistics import median

position_list = []
for i in range(100000000):
    value = randint(1,10)
    position_list.append(value)
    
print(mean(position_list))
print(median(position_list))

# print(position_list[1:5000])