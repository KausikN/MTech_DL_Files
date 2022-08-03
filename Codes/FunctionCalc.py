'''
Calculating Function Values
'''

# Imports
from email.mime import base
import numpy as np

# Main Functions
def LossFunc_RMSE(y_pred, y_true):
    term_sub = y_pred - y_true
    term_sq = term_sub**2
    term_mean = np.mean(term_sq, axis=-1)
    term_sqrt = np.sqrt(term_mean)
    print(term_sub)
    print(term_sq)
    print(term_mean)
    print(term_sqrt)
    return np.sum(term_sqrt)

def LossFunc_CrossEntropy(y_pred, y_true, log_base=10):
    term_log = np.log(y_pred) / np.log(log_base)
    term_mul = y_true * term_log
    term_sum = np.sum(term_mul, axis=-1)
    print(term_log)
    print(term_mul)
    print(term_sum)
    return -np.sum(term_sum)

# Driver Code
# RMSE ###################################################################################################
X = np.array([
    [0.5],
    [0.63],
    [0.25],
    [0.8],
    [0.55]
])
Y = np.array([
    [0.4],
    [0.6],
    [0.35],
    [0.85],
    [0.63]
])
print("RMSE:", LossFunc_RMSE(X, Y))
print("\n")
# RMSE ###################################################################################################

# Cross Entropy ##########################################################################################
X = np.array([
    [50, 25, 25]
])/100
Y = np.array([
    [40, 40, 20]
])/100
LOG_BASE = 2
print("Cross Entropy:", LossFunc_CrossEntropy(X, Y, log_base=LOG_BASE))
print("\n")
# Cross Entropy ##########################################################################################