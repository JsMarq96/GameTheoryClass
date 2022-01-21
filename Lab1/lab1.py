#!/usr/bin/env python3

'''
  ACTIVITY 1
'''
import nashpy as nash
import numpy as np

print('Activity 1: ========')

p1 = np.array([[-1, -3], [0, -2]])
p2 = np.array([[-1, 0], [-3, -2]])

prisioner_dilema = nash.Game(p1, p2)

print(prisioner_dilema)

eqs = prisioner_dilema.support_enumeration()
print(list(eqs))


'''
 ACTIVITY 2
  The penny's game
  A zero-sum game: the sum of the utility matricies is 0
'''

print('\n\nActivity 2: ===========')

p1 = np.array([[1, -1], [-1, 1]])
p2 = np.array([[-1, 1], [1, -1]])

matching_pennies = nash.Game(p1, p2)

print(matching_pennies)
print(list(matching_pennies.support_enumeration()))


print('\n\n Activiy 3: ==========')
'''
 Hay equilibrios de nash en elegir FutFut o OperaOpera
'''
h = np.array([[3, 0], [0, 2]])
w = np.array([[2, 0], [0, 3]])

BoS = nash.Game(h, w)

print(BoS)
print(list(BoS.support_enumeration()))
