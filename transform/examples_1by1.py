import numpy as np
import matplotlib.pyplot as plt
import copy

from src import transform
from src import utils

if __name__ == "__main__":
    
    matrix = np.matrix([1]).reshape(1,1)
    meantrans = transform.Meantrans(matrix)
    meantrans.compute(10)
    matrix_list = meantrans.result
    
    transform.get_info(matrix_list[1])
    