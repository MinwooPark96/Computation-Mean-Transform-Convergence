import numpy as np
import matplotlib.pyplot as plt
import copy
# from collections import defaultdict 

from typing import Union

M = np.matrix 

def get_SVD(T:M):
    w,sigma,v_h = np.linalg.svd(T)
    sigma = np.diag(sigma)    
    return w,sigma,v_h

def get_duggal(T:M):
    w,sigma,v_h = get_SVD(T)    
    v = v_h.H
    I = np.logical_not(np.isclose(sigma,0))
    u = w@I@v_h
    
    abs = v@sigma@v_h
    return abs@u

def get_mean(T:M,s=0.5,t=0.5):
    return s*T + t*get_duggal(T)

def get_norm(T:M):
    return np.linalg.norm(T)

def get_characteristic(T:M):
    distance = T @ T.H - T.H @ T
    return get_norm(distance)
                

class MeanTransform:
    
    def __init__(self,T):
        self.T = T
        
        self.sequence = list()
        self.norm_list = list() 
        self.normal_characteristic_list = list() 
        
        self.COMPUTED = 0
        
    def compute(self, n=0, s=0.5, t=0.5): # n : iteration count                 
        
        self.n=n
        self.COMPUTED = n
        self.sequence.append(self.T)
        
        self.k = 4
        
        for _ in range(self.n):    
            T_hat = get_mean(self.sequence[-1])
            self.sequence.append(T_hat)
            
        for T in self.sequence:
            norm = get_norm(T)
            ch = get_characteristic(T)
        
            self.norm_list.append(norm)
            self.normal_characteristic_list.append(ch)

            
    def print_one_matrix(self,i : int):
        if not self.sequence:
            print('not computed yet. please run compute() method') 
        T  = self.sequence[i]
        MeanTransform.print_helper(T,'T_'+str(i)+' = ')
    
    @staticmethod
    def print_helper(T:M , head : Union[str,None] = None,k=4):
        rounded_T = np.round(T,k)
        if head is not None:
            print(head)
        for row in rounded_T:
            print(row)
        print()
    
    @staticmethod
    def verbose_helper(T:M,k=4):
        
        w,sigma,v_h = get_SVD(T)
        v = v_h.H
        I = np.logical_not(np.isclose(sigma,0)).astype(int)
        u = w@I@v_h
        
        PRINT_DICT = {'T=':T,'w = ':w,'sigma = ':sigma,'v_h = ':v_h,'v = ':v,'I = ':I,'u = ':u,'mean = ':get_mean(T),'F = ':get_characteristic(T) }
        
        for key in PRINT_DICT.keys():
            print(key)
            MeanTransform.print_helper(T,PRINT_DICT[key],k=k)
        
        print('F = ',get_characteristic(T),end = '\n\n')

    def print_all_matrix(self):
        for i in range(self.n):
            self.print_one_matrix(i)
    
    def get_matrix(self,i:int) -> Union[M,None]:
        
        if self.n -1 >= i :
            return self.sequence[i]
        
        return None
    
    def get_sequence(self):
        return self.sequence
    
    def get_norm(self):
        return self.norm_list
    
    def get_normal_characteristic(self):
        return self.normal_characteristic_list
    
    
    def set_round(self,k):
        self.k = k
        
    def __getitem__(self,i):
        assert i < self.n, 'index out of range'
        return self.get_matrix(i)
    
    def __len__(self):
        return self.n
    
    def __iter__(self):
        return iter(self.sequence)

    
    
#test code
if __name__ == "__main__":
    
    T = np.matrix([0, 27890, 0, 0]).reshape(2, 2)
    
    meantrans = MeanTransform(T)
    meantrans.compute(n=10)
    
    
    for m in meantrans:
        meantrans.verbose_helper(m)
    
