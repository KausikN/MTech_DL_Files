'''
1D Sigmoid Functions Comparison
'''

# Import
import numpy as np
import matplotlib.pyplot as plt

# Main Functions
def Sigmoid_1D(x, a, b):
    return 1 / (1 + np.exp(-(a*x + b)))

def PlotSigmoids_1D(SigmoidParams, x_range=(-5.0, 5.0), n_points=100):
    X = np.linspace(x_range[0], x_range[1], n_points)
    plt.figure(figsize=(10, 10))
    for i in range(len(SigmoidParams)):
        Y = Sigmoid_1D(X, SigmoidParams[i][0], SigmoidParams[i][1])
        plt.plot(X, Y, label="a={}, b={}".format(SigmoidParams[i][0], SigmoidParams[i][1]))
    plt.legend()
    plt.show()

# Driver Code
# Params
SigmoidParams = [
    [10, 5],
    [30, 5],
    [10, -5],
    [30, -5],
    # [30, 0],
    # [10, 0]
]

X_RANGE = (-5.0, 5.0)
N_POINTS = 100
# Params

# RunCode
PlotSigmoids_1D(SigmoidParams, x_range=X_RANGE, n_points=N_POINTS)