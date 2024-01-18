import numpy as np
import matplotlib.pyplot as plt
import copy


from src import transform
from src import utils

if __name__ == "__main__":
    
    matrix6 = np.matrix([1, 2, 3, 4 ,
                              8, 7, 6, 5 ,
                              9, 10, 11, 12,
                              16, 15, 14, 13]).reshape(4, 4)    
    meantrans6 = transform.Meantrans(matrix6)
    meantrans6.compute(100)
    matrix_list6 = meantrans6.get_matrix_list(is_np = False)
    utils.save(meantrans=meantrans6, name = 'ex6')
    
    
    