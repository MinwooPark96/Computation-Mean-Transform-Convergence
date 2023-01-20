
import numpy as np
import matplotlib.pyplot as plt
import copy

class Transformation():
    
    def __init__(self):
        
        self.color_dict={0:"magenta",1:"dimgray",2:"cyan"}
        self.type_dict={0:"Aluthge",1:"Duggal",2:"Mean"}
        self.type_dict_2= {v: k for k, v in self.type_dict.items()}

    def cycle(self,T,Type): # one iteration
        
        #Singular Value Decomposition
        w,sigma,v_h=np.linalg.svd(T)    
        sigma=np.diag(sigma) 
        v=v_h.H
        
        sigma_sq=np.sqrt(sigma)
        sigma_hat=v@sigma_sq@v_h 
        sigma_pinv=np.linalg.pinv(sigma)
        
        #Check which U do you want; unitary or partial isometry
        if self.isometry:
            u=w@sigma@sigma_pinv@v_h
        else :
            u=w@v_h
        
        T_abs=v@sigma@v_h
        
        #Compute each Transformation
        T_tilda=sigma_hat@u@sigma_hat
        T_duggal=T_abs@u
        T_mean=1/2*(T+T_duggal)
        
        if Type=="Aluthge":
            output=T_tilda
        elif Type=="Duggal":
            output=T_duggal
        else :
            output=T_mean
        
        return output #one epoch output
             
    def Transform(self,T,n=1,isometry=True): # n : iteration count 
        self.isometry=isometry
        Type_list=["Aluthge","Duggal","Mean"]
        
        self.T=T
        self.n=n
        self.total_info=[]

        for j in Type_list:
            before=copy.deepcopy(self.T)
        
            cal_info=[T]
        
            for i in range(self.n):
                
                after=self.cycle(before,Type=j)
                cal_info.append(after)
                before=after
            
            self.total_info.append(cal_info)
        
        self.Aluthge_info=self.total_info[0]
        self.Duggal_info=self.total_info[1]
        self.Mean_info=self.total_info[2]
        
    def Normal_calculator(self): 
        self.norm_info=[[],[],[]] #list of Frobenius norm of each transformation output matrix
        self.normal_info=[[],[],[]] #list of Frobenius norm of each transformation output matrix
        
        for i in range(3):
            for j in self.total_info[i]:
                norm=np.linalg.norm(j)
                distance_matrix=np.abs(j@j.H-j.H@j)
                distance=np.linalg.norm(distance_matrix)
                self.normal_info[i].append(distance)
                self.norm_info[i].append(norm)
    
    
    def Normal_plot(self):

        self.total_fig, self.total_ax=plt.subplots(1,1)
        
        for i in range(3):
            self.total_ax.plot(range(self.n+1),self.normal_info[i],color=self.color_dict[i],\
                               label=self.type_dict[i],alpha=0.5,marker="o",linestyle="dashed")
            self.total_ax.set_title("Normal Characteristic")
        
        self.total_fig.set_size_inches((16,8))
        self.total_ax.grid(axis='x', color='0.95',linestyle="--")
        self.total_ax.legend(title="Type")

        
    def Process(self,k,Type,digit=4): #Method that check caculation process for each iteration
        print("===============<START>===============\n")

        M=self.total_info[self.type_dict_2[Type]][k-1]
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
        
        else :
            u=w@v_h
            print("U=WV^*\n",np.round(u,digit),"\n")
        
    
        T_abs=v@sigma@v_h
        
        print("|T|\n",np.round(T_abs,digit),"\n")
        
        print("U|T|\n",np.round(u@T_abs,digit),"\n")

        if Type=="Aluthge":
            T_tilda=sigma_hat@w@v_h@sigma_hat
            print(f"T_hat({k}) : Aluthge\n",np.round(T_tilda,digit),"------->(a)\n")
        
        elif Type=="Duggal":
        
            T_duggal=T_abs@u
            print(f"T_hat({k}) : Duggal\n",np.round(T_duggal,digit),"------->(a)\n")
        else :
            T_abs@u
            T_mean=(M+T_abs@u)/2
            
            print("|T|U",np.round(T_abs@u,digit),"\n")
            print(f"T_hat({k}) : Mean\n",np.round(T_mean,digit),"------->(a)\n")
        
        print("result from our Method\n",np.round(self.total_info[self.type_dict_2[Type]][k],4),"------->(b)")
        print("If (a)!=(b), Error.. ; If that happens, please send email us")
        print("E-mail : alsdn0110@snu.ac.kr")
        
        