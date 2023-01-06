import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import copy


# st weighted Transform
class Weighted_Transformation():
    
    def __init__(self):
        
        self.color_dict={0:"magenta",1:"dimgray",2:"cyan"}
        self.type_dict={0:"st_weighted"}
        self.type_dict_2= {v: k for k, v in self.type_dict.items()}
        
        
    def Epoch(self,T): # one iteration 
        
        w,sigma,v_h=np.linalg.svd(T)    
        sigma=np.diag(sigma) 
        v=v_h.H
        
        sigma_sq=np.sqrt(sigma)
        sigma_hat=v@sigma_sq@v_h 
        sigma_pinv=np.linalg.pinv(sigma)
        #default u -> isometry
        if self.isometry:
            u=w@sigma@sigma_pinv@v_h
        else:
            u=w@v_h
        
        T_abs=v@sigma@v_h
        T_duggal=T_abs@u
        T_st=(self.s*T+self.t*T_duggal)
        
        
        return T_st #one epoch output
             
    def Transform(self,T,n=1,s=1/2,t=1/2,isometry=True): # n : iteration count 
        
        self.s=s
        self.t=t
        self.T=T
        self.n=n
        self.isometry=isometry
        
        before=copy.deepcopy(self.T)
        
        self.st=[T]
            
        for i in range(self.n):
                
            after=self.Epoch(before)
            self.st.append(after)
            before=after
            
    def Normal_calculator(self): 
        self.norm_info=[] #list of Frobenius norm of each transformation output matrix
        self.normal_info=[] #list of Frobenius norm of each transformation output matrix
        
        for j in self.st:
            norm=np.linalg.norm(j)
            distance_matrix=np.abs(j@j.H-j.H@j)
            distance=np.linalg.norm(distance_matrix)
            self.normal_info.append(distance)
            self.norm_info.append(norm)
    
    
    def Normal_plot(self): # plot that dipicts Frobenius norm of T(T^*)-(T^*)T

        self.total_fig, self.total_ax=plt.subplots(1,1)
        
        self.total_ax.plot(range(self.n+1),self.normal_info,color="b",alpha=0.5,marker="o",linestyle="dashed")
        self.total_ax.set_title("Normal Characteristic")
        
        self.total_fig.set_size_inches((16,4))
        self.total_ax.grid(axis='x', color='0.95',linestyle="--")
        
    def Process(self,k,digit=4):
        
        print("===============<START>===============\n")
        
        M=self.st[k-1]
        print(f"T_hat({k-1})\n",np.round(M,digit),"\n")
        
        w,sigma,v_h=np.linalg.svd(M)   
        sigma=np.diag(sigma) 
        v=v_h.H
        
        print("W\n",np.round(w,digit),"\n")
        print("Sigma\n",np.round(sigma,digit),"\n")
        print("V_h\n",np.round(v_h,digit),"\n")
        print("W\Sigma V^*\n",np.round(w@sigma@v_h,digit),"\n")
        print("WV^*\n",np.round(w@v_h,digit),"\n")
        print("V\n",v,"\n")
        
        sigma_sq=np.sqrt(sigma)
        sigma_hat=v@sigma_sq@v_h
        sigma_pinv=np.linalg.pinv(sigma)
        if self.isometry:
            u=w@sigma@sigma_pinv@v_h
            print("U=W\Sigma\Sigma_pinv V^*\n",np.round(u,digit),"\n")
        else:    
            u=w@v_h
            print("U=WV^*\n",np.round(u,digit),"\n")
        
        
        T_abs=v@sigma@v_h
        
        print("|T|\n",np.round(T_abs,digit),"\n")
        
        print("U|T|\n",np.round(u@T_abs,digit),"\n")

     
        T_duggal=T_abs@u
        print("T_duggal\n",np.round(T_duggal,digit),"\n")
        
        T_st=(self.s*M+self.t*T_abs@u)
            
        print("|T|U",np.round(T_abs@u,digit),"\n")
        print(f"T_hat({k})\n",np.round(T_st,digit),"------->(a)\n")
        
        
        print("===============<END>===============\n")
        print("result from our Method  \n",np.round(self.st[k],digit),"------->(b)")
        print("If a!=b, Error.. ; If that happens, please email us")
        print("e-mail : alsdn0110@snu.ac.kr")
        
    def __getitem__(self,key):
        return self.st[key]