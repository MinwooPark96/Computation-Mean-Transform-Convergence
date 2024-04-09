import numpy as np
import matplotlib.pyplot as plt
import copy

from src import transform
from src import utils


def append_with_copy(l,item):
    l.append(copy.deepcopy(item))


def generate_exmaple_1by1() -> list[transform.MeanTransform]:
    example = list()
    T = matrix = np.matrix([1]).reshape(1,1)
    append_with_copy(example, T)
    return example

def generate_exmaple_2by2() -> list[transform.MeanTransform]:
    example = list()
    
    T = matrix = np.matrix([0, 27890, 0, 0]).reshape(2, 2)
    append_with_copy(example, T)
    
    T = matrix = np.matrix([0, 1, 0, 0]).reshape(2, 2)
    append_with_copy(example, T)
    
    T = matrix = np.matrix([complex(0,1),2,0,complex(0,-1)]).reshape(2,2)
    append_with_copy(example, T)
    
    T = matrix = np.matrix([complex(0,1),2,0,complex(0,-1)]).reshape(2,2)
    append_with_copy(example, T)
    
    return example

def generate_exmaple_3by3() -> list[transform.MeanTransform]:
    example = list()
    
    T = matrix = np.matrix([1, 2, 3,
                              6,5,4,
                              7,8,9]).reshape(3, 3)    
    append_with_copy(example, T)
    return example

def generate_exmaple_4by4() -> list[transform.MeanTransform]:
    example = list()
    
    T = np.matrix([1, 2, 3, 4 ,
                              8, 7, 6, 5 ,
                              9, 10, 11, 12,
                              16, 15, 14, 13]).reshape(4, 4)    
    
    append_with_copy(example, T)
    return example

def generate_example_random(start_seed = 42, number_of_example = 10, dim = 2) -> list[transform.MeanTransform]:
    example = list()
    seed = start_seed
    for _ in range(number_of_example):
        random_complex_matrix = utils.generate_random_complex(dim, seed)
        append_with_copy(example, random_complex_matrix)
    seed+=1
    return example    

if __name__ == "__main__":
        
    example = generate_example_random(start_seed=42, number_of_example=100, dim=2)
    for i, T in enumerate(example):
        meantrans = transform.MeanTransform(T)
        meantrans.compute(100)
        # meantrans.print_all_matrix()
        
        normal_ch = meantrans.get_normal_characteristic()
        assert utils.is_decreasing(normal_ch)
    
    # utils.save(meantrans=meantrans, name='example')
        