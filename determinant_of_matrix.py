import numpy.linalg as m
import numpy as np
def determinant(mtx):
    return round(m.det(np.matrix(mtx)))