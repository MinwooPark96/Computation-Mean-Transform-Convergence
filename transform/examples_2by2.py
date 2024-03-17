import numpy as np
import matplotlib.pyplot as plt
import copy

from src import transform
from src import utils

if __name__ == "__main__":
    
    # matrix1 = np.matrix([0, 27890, 0, 0]).reshape(2, 2)    
    # meantrans1 = transform.Meantrans(matrix1)
    # meantrans1.compute(100)
    # matrix_list1 = meantrans1.result
    # utils.save(meantrans=meantrans1, name = 'ex1')
    
    
    # matrix2 = np.matrix([0, 1, 0, 0]).reshape(2, 2)
    # meantrans2 = transform.Meantrans(matrix1)
    # meantrans2.compute(100)
    # matrix_list2 = meantrans2.result
    # utils.save(meantrans=meantrans2, name = 'ex2')
    
    # matrix3 = np.matrix([0, 1, 0, 0]).reshape(2, 2)
    # meantrans3 = transform.Meantrans(matrix3)
    # meantrans3.compute(100)
    # matrix_list3 = meantrans3.result
    # utils.save(meantrans=meantrans3, name = 'ex3')
    
    # matrix4 = np.matrix([complex(0,1),2,0,complex(0,-1)]).reshape(2,2)
    # meantrans4 = transform.Meantrans(matrix4)
    # meantrans4.compute(100)
    # matrix_list4 = meantrans4.result
    # utils.save(meantrans=meantrans4, name = 'ex4')
    
    matrix5 = np.matrix([2,-1,3,4]).reshape(2,2)
    meantrans5 = transform.Meantrans(matrix5)
    meantrans5.compute(3)
    matrix_list5 = meantrans5.result
    utils.save(meantrans=meantrans5, name = 'ex5')
    
    transform.get_info(matrix_list5[1])
    