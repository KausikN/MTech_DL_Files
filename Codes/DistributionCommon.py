'''
Finds common point of 2 distributions
'''

# Import
from math import log

# Main Functions
def CommonPoints_Normal(m1, s1, m2, s2):
    t1 = 2 * (s1**2 - s2**2) * log(s1 / s2)
    t2 = (m1 - m2)**2 + t1
    t3 = m1*s2 + s1 * (t2**(0.5))
    t4 = m2*(s1**2) - s2*(t3)
    c = t4 / (s1**2 - s2**2)
    return c

# Driver Code
# Params
m1, s1 = 2.5, 1.5
m2, s2 = 6.0, 0.75
# Params

# RunCode
print(CommonPoints_Normal(m1, s1, m2, s2))