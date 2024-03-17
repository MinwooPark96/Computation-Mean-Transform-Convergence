import numpy as np
import matplotlib.pyplot as plt
import copy
# from collections import defaultdict 


def get_SVD(T):
    w,sigma,v_h = np.linalg.svd(T)
    sigma = np.diag(sigma)
    
    return w,sigma,v_h

def get_duggal(T):
    w,sigma,v_h = get_SVD(T)
    
    v = v_h.H
    I = np.logical_not(np.isclose(sigma,0))
    u = w@I@v_h
    
    abs = v@sigma@v_h
    return abs@u

def get_mean(T,s=0.5,t=0.5):
    return s*T + t*get_duggal(T)

def get_norm(T):
    return np.linalg.norm(T)

def get_characteristic(T):
    distance = T @ T.H - T.H @ T
    return get_norm(distance)
            

def print_matrix(T):
        for row in T:
            print(row)
        print()

def get_info(T):
    w,sigma,v_h = get_SVD(T)
    v = v_h.H
    I = np.logical_not(np.isclose(sigma,0))
    u = w@I@v_h
    
    print('T=')
    print_matrix(T)
    
    print('w = ')
    print_matrix(w)
    
    print('sigma = ')
    print_matrix(sigma)
    
    print('v_h = ')
    print_matrix(v_h)
    
    print('v = ')
    print_matrix(v)
    
    print('I = ')
    print_matrix(I)
    
    print('u = ')
    print_matrix(u)
    
    print('mean = ')
    print_matrix(get_mean(T))
    
    print('F = ')
    print(get_characteristic(T))
    
    

class Meantrans:
    
    def __init__(self,T):
        self.T = T
        
        self.result = list()
        self.norm_list = list() 
        self.normal_characteristic_list = list() 
        
    def compute(self, n=0, s=0.5, t=0.5): # n : iteration count                 
        
        self.n=n
        self.result.append(self.T)
        
        for _ in range(self.n):    
            T_hat = get_mean(self.result[-1])
            self.result.append(T_hat)
            
        for T in self.result:
            norm = get_norm(T)
            ch = get_characteristic(T)
        
            self.norm_list.append(norm)
            self.normal_characteristic_list.append(ch)

            
    def get_info(self,i : int):
        if not self.result:
            return 
        T  = self.result[i]
        w,sigma,v_h = get_SVD(T)
        
    
    def get_matrix(self,i):
        if self.n -1 >= i :
            return self.result[i]
        return 
    
    #test code
if __name__ == "__main__":
    
    T = np.matrix([0, 27890, 0, 0]).reshape(2, 2)
    
    meantrans = Meantrans(T)
    meantrans.compute(n=0)
    meantrans.compute(n=10)
    
    
    for matrix_objects in meantrans.matrix_list:
        print(matrix_objects.matrix)
    
    matrix_list_np = meantrans.get_matrix_list(is_np=True)
    for i in matrix_list_np:
        print(type(i))
        
    print(meantrans.norm_list)
    print(meantrans.normal_characteristic_list)
    
