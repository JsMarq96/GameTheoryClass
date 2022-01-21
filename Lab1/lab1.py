#!/usr/bin/env python3
import nashpy as nash
import numpy as np

p1 = np.array([[-1, -3], [0, -2]])
p2 = np.array([[-1, 0], [-3, -2]])

prisioner_dilema = nash.Game(p1, p2)

print(prisioner_dilema)

eqs = prisioner_dilema.support_enumeration()
print(list(eqs))
