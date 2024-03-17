import numpy as np
import matplotlib.pyplot as plt
import copy


from src import transform
from src import utils

if __name__ == "__main__":
    
    matrix10 = np.matrix([1, 2, 3,
                              6,5,4,
                              7,8,9]).reshape(3, 3)    
    meantrans10 = transform.Meantrans(matrix10)
    meantrans10.compute(10)
    matrix_list10 = meantrans10.result
    utils.save(meantrans=meantrans10, name = 'ex10')
    
        
    transform.get_info(matrix_list10[0])
    w,sigma,v_h = transform.get_SVD(matrix_list10[0])
    