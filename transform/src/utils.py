import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import seaborn as sns
import pandas as pd

from src import transform

def save(meantrans : transform.Meantrans, name):
    
    assert isinstance(meantrans,transform.Meantrans) == True

    plt.figure(figsize=(16,4))
    
    df = pd.DataFrame({'norm':meantrans.normal_characteristic_list,"iter":range(meantrans.n+1)})
    df.set_index('iter',inplace=True)
    
    ax = sns.lineplot(data = df, x = 'iter', y='norm',lw = 2.5,
                 dashes = False, markersize = 8 , markers=['o']
                )
    for axis in ['bottom', 'left']:
        ax.spines[axis].set_linewidth(2.5)
        ax.spines[axis].set_color('0.2')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.tick_params(width = 2.5, color = '0.2')

    # plt.xticks(size = 14, weight = 'bold', color = '0.2')
    # plt.yticks(size = 14, weight = 'bold', color = '0.2')
    
    plt.xlim(0,meantrans.n)
    
    # plt.yscale('log')
    
    plt.locator_params(axis='x', nbins=meantrans.n/10)

    ax.set_xlabel(ax.get_xlabel(), fontsize = 14, weight = 'bold', color = '0.2')
    ax.set_ylabel(ax.get_ylabel(), fontsize = 14, weight = 'bold', color = '0.2')
    
    plt.grid(True,linestyle = '--',linewidth=0.5)
    
    title_font = {
    'fontsize': 16,
    'fontweight': 'bold'
    }
    plt.title("The Normal Characteristic of Matrix", fontdict=title_font, loc='left', pad=20)
    
    # total_ax.plot(range(meantrans.n+1),meantrans.normal_characteristic_list,color="b",alpha=0.5,marker="o",linestyle="dashed")
    
    os.makedirs('figure',exist_ok=True)
    plt.savefig('figure/'+name+'.png', bbox_inches = 'tight', dpi = 250, facecolor = ax.get_facecolor())

    os.makedirs('csv',exist_ok=True)
    df.to_csv('csv/'+name+'.csv')
    
    
if __name__ == '__main__':
    T = np.matrix([2, -1, 3, 4]).reshape(2, 2)
    
    meantrans = transform.Meantrans(T)
    meantrans.compute(n=0)
    meantrans.compute(n=50)
    
    print(plot(meantrans))
    