import numpy as np
import matplotlib.pyplot as plt
import copy
class MeanTrans():
    
    def __init__(self):

        self.color_dict = {0:"magenta",1:"dimgray",2:"cyan"}
        self.type_dict = {0:"st_weighted"}

    def cycle(self,T):
        
        w,sigma,v_h = np.linalg.svd(T)
        sigma = np.diag(sigma)
        v = v_h.H
        
        sigma_sq = np.sqrt(sigma)
        sigma_hat = v@sigma_sq@v_h
        sigma_pinv = np.linalg.pinv(sigma)

        if self.isometry:
            u = w@sigma@sigma_pinv@v_h
        else:
            u = w@v_h
        
        T_abs = v@sigma@v_h
        T_duggal = T_abs@u
        T_st = (self.s*T+self.t*T_duggal)

        return T_st
             
    def transform(self, T, n=1, s=1/2, t=1/2, isometry=True): # n : iteration count
        
        self.s = s
        self.t = t
        self.T = T
        self.n = n
        self.isometry = isometry
        
        before = copy.deepcopy(self.T)
        
        self.st = [T]
            
        for i in range(self.n):
                
            after = self.cycle(before)
            self.st.append(after)
            before = after
            
    def normal_calculator(self):
        self.norm_info = [] #list of Frobenius norm of each transformation output matrix
        self.normal_info = [] #list of Frobenius norm of each transformation output matrix
        
        for j in self.st:
            norm = np.linalg.norm(j)
            distance_matrix = np.abs(j@j.H-j.H@j)
            distance = np.linalg.norm(distance_matrix)
            self.normal_info.append(distance)
            self.norm_info.append(norm)
    
    
    def normal_plot(self): # plot that dipicts Frobenius norm of T(T^*)-(T^*)T

        self.total_fig, self.total_ax=plt.subplots(1,1)
        
        self.total_ax.plot(range(self.n+1),self.normal_info,color="b",alpha=0.5,marker="o",linestyle="dashed")
        self.total_ax.set_title("Normal Characteristic")
        self.total_fig.set_size_inches((16,4))
        self.total_ax.grid(axis='x', color='0.95',linestyle="--")
        
    def process(self, k, dicimals=4):
        if k == 0 or k > self.n:
            raise Exception("k must be more than 0 and less than n.")
        print("===============<START>===============\n")
        
        M=self.st[k-1]
        print(f"T_hat({k-1})\n", np.round(M, dicimals), "\n")
        
        w,sigma,v_h=np.linalg.svd(M)   
        sigma=np.diag(sigma) 
        v=v_h.H
        
        print("W\n", np.round(w, dicimals), "\n")
        print("Sigma\n", np.round(sigma, dicimals), "\n")
        print("V_h\n", np.round(v_h, dicimals), "\n")
        print("W\Sigma V^*\n", np.round(w @ sigma @ v_h, dicimals), "\n")
        print("WV^*\n", np.round(w @ v_h, dicimals), "\n")
        print("V\n",v,"\n")
        
        sigma_sq=np.sqrt(sigma)
        sigma_hat=v@sigma_sq@v_h
        sigma_pinv=np.linalg.pinv(sigma)
        if self.isometry:
            u=w@sigma@sigma_pinv@v_h
            print("U=W\Sigma\Sigma_pinv V^*\n", np.round(u, dicimals), "\n")
        else:    
            u=w@v_h
            print("U=WV^*\n", np.round(u, dicimals), "\n")
        
        
        T_abs=v@sigma@v_h
        
        print("|T|\n", np.round(T_abs, dicimals), "\n")
        
        print("U|T|\n", np.round(u @ T_abs, dicimals), "\n")

     
        T_duggal=T_abs@u
        print("T_duggal\n", np.round(T_duggal, dicimals), "\n")
        
        T_st=(self.s*M+self.t*T_abs@u)
            
        print("|T|U", np.round(T_abs @ u, dicimals), "\n")
        print(f"T_hat({k})\n", np.round(T_st, dicimals), "------->(a)\n")
        
        
        print("===============<END>===============\n")
        print("result from our Method  \n", np.round(self.st[k], dicimals), "------->(b)")
        print("If a!=b, Error.. ; If that happens, please email us")
        print("e-mail : alsdn0110@snu.ac.kr")
        
    def __getitem__(self,key):
        return self.st[key]

#test code
if __name__ == "__main__":
    T = np.matrix([0, 27890, 0, 0]).reshape(2, 2)
    Transformer = MeanTrans()
    Transformer.transform(T, 10)

    print(Transformer[10])
    Transformer.process(1)
    Transformer.normal_calculator()
    Transformer.normal_plot()
