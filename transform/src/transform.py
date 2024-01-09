import numpy as np
import matplotlib.pyplot as plt
import copy
# from collections import defaultdict 



class Matrix():
    
    def __init__(self,matrix : np.matrix, s=0.5, t=0.5):
        self.matrix = matrix
        
        #svd
        self.w,sigma,self.v_h = np.linalg.svd(self.matrix)
        self.sigma = np.diag(sigma)
        
        self.v = self.v_h.H
        
        self.sigma_sq = np.sqrt(self.sigma)
        
        self.indicator = np.logical_not(np.isclose(self.sigma,0))
        
        self.u = self.w@self.indicator@self.v_h
        
        self.abs = self.v@self.sigma@self.v_h
        self.duggal = self.abs@self.u
        self.mean = s*self.matrix+t*self.get_duggal()
    
    def get_duggal(self):
        return self.duggal

    def get_mean(self):
        return copy.deepcopy(self.mean)
    
    def __str__(self):
        return self.matrix
    
class Meantrans():
    
    def __init__(self,matrix):
        self.matrix = matrix
        
        self.matrix_list = list()
        self.norm_list = list() 
        self.normal_characteristic_list = list() 
        
        
    def compute(self, n=0, s=0.5, t=0.5): # n : iteration count                 
        
        #init
        if len(self.matrix_list) == 0:  
            self.n=n
            self.matrix_list.append(Matrix(self.matrix))
            for _ in range(n):    
                next_matrix : np.matrix = self.matrix_list[-1].get_mean()
                self.matrix_list.append(Matrix(next_matrix))
            
            for matrix in self.matrix_list:
                norm = np.linalg.norm(matrix.matrix)
                distance_matrix = matrix.matrix @ matrix.matrix.H - matrix.matrix.H @ matrix.matrix
                distance = np.linalg.norm(distance_matrix)
            
                self.norm_list.append(norm)
                self.normal_characteristic_list.append(distance)

        elif len(self.matrix_list) >= n+1:
            print('already computed')
                        
        else :
            self.n = n
            for _ in range(n-len(self.matrix_list)+1):
                next_matrix : np.matrix = self.matrix_list[-1].get_mean()
                self.matrix_list.append(Matrix(next_matrix))
                
                norm = np.linalg.norm(next_matrix)
                distance_matrix = next_matrix @ next_matrix.H - next_matrix.H @ next_matrix
                distance = np.linalg.norm(distance_matrix)
            
                self.norm_list.append(norm)
                self.normal_characteristic_list.append(distance)

                
    def get_matrix_list(self,is_np = True):
        if not is_np :
            return self.matrix_list
        return [matrix.matrix for matrix in self.matrix_list]
        
    
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