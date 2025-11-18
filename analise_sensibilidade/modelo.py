import numpy as np

def funcao_1(X, params):
    """Non-monotonic Ishigami-Homma three parameter test function"""

    a = params[0]
    b = params[1]

    Y = np.sin(X[:, 0]) + a * np.power(np.sin(X[:, 1]), 2) + \
        b * np.power(X[:, 2], 4) * np.sin(X[:, 0])

    return Y