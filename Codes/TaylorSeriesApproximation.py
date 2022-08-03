'''
Taylor Series Approximation
'''

# Import
from math import factorial
from tqdm import tqdm

# Main Functions
def TaylorSeriesApprox_PowerN(a, da, n, n_terms=2):
    '''
    By Taylor Series Expansion,
    (a + da)^n = a^n + da * n * a^(n-1) + da^2 * n * (n-1) * a^(n-2) + ...
    '''
    data = []
    val = 0.0
    for i in tqdm(range(n_terms)):
        term_n = 1.0
        for j in range(i):
            term_n *= n-j
        term_a = a**(n-i)
        term_da = da**i
        term_denom = factorial(i)
        val += (term_a * term_da) * (term_n/term_denom)
        data.append((term_a, term_da, term_n, term_denom))
    return val, data

# Driver Code
# Params
N_TERMS = 3

a = 3.0
da = 0.0001
n = 3
# Params

# RunCode
val, data = TaylorSeriesApprox_PowerN(a, da, n, n_terms=N_TERMS)
print("Actual Value:", (a+da)**n)
print("Predicted Value:", val)
for i in range(N_TERMS):
    print(i, ":", data[i])