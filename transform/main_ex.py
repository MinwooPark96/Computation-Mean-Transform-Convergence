import numpy as np
import matplotlib.pyplot as plt
import copy

from src import transform
from src import utils

def example_2_2():
    T = matrix = np.matrix([complex(0,1),2,0,complex(0,-1)]).reshape(2,2)
    return T

def example_2_5():
    T = matrix = np.matrix([0, 1, 0, 0]).reshape(2, 2)
    return T

def example_2_6():
    T = matrix = np.matrix([0, 1, 0, 1]).reshape(2, 2)
    return T

def example_3_1():
    T = matrix = np.matrix([2, -1, 3, 4]).reshape(2, 2)
    return T
    
def example_3_3():
    T = matrix = np.matrix([1, 2, 3,
                              6,5,4,
                              7,8,9]).reshape(3, 3)    
    return T

if __name__ == "__main__":
        
    T = example_3_3()
    
    meantrans = transform.MeanTransform(T)
    
    meantrans.compute(5)
    
    normal_ch = meantrans.get_normal_characteristic()
    
    assert utils.is_decreasing(normal_ch)
    
    meantrans.print_all_matrix()
    
    meantrans.verbose(0)
    
    
    # utils.save(meantrans=meantrans, name='example')
        