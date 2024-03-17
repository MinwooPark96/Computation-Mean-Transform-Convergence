import numpy as np
import matplotlib.pyplot as plt
import copy


from src import transform
from src import utils

if __name__ == "__main__":
    
    random_complex_matrix = utils.generate_random_complex(4) #4x4
    meantrans7 = transform.Meantrans(random_complex_matrix)
    meantrans7.compute(10)
    matrix_list7 = meantrans7.get_matrix_list(is_np = False)
    utils.save(meantrans=meantrans7, name = 'ex7')
    
    random_complex_matrix = utils.generate_random_complex(10) #4x4
    meantrans8 = transform.Meantrans(random_complex_matrix)
    meantrans8.compute(10)
    matrix_list8 = meantrans8.get_matrix_list(is_np = False)
    utils.save(meantrans=meantrans8, name = 'ex8')
    
    
    
    
    