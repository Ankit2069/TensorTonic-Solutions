import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    if A.shape[0] != A.shape[1]:
        raise ValueError("No Trace : Matrix is not square")

    return np.trace(A)
    pass