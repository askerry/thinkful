
import scipy.stats
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

def print_frequencies(data):
    counts=Counter(data)
    for i in sorted(counts.keys()):
        print "probability of %s: %.3f" %(i, float(counts[i])/np.sum(counts.values()))
        
def save_boxplot(data):
    f,ax=plt.subplots(figsize=[3,4])
    ax.set_ylim([0,10])
    sns.boxplot(data, ax=ax)
    ax.set_xticks([])
    ax.set_title('boxplot')
    plt.tight_layout()
    plt.savefig("../figs/data_boxplot.png")
    
def save_histogram(data):
    f,ax=plt.subplots(figsize=[4,4])
    ax.hist(data)
    ax.set_label('frequency')
    ax.set_title('histogram')
    plt.tight_layout()
    plt.savefig("../figs/data_hist.png")
    
def save_qqplot(data):
    f,ax=plt.subplots(figsize=[4,4])
    scipy.stats.probplot(data, dist="norm", plot=plt)
    ax.set_title('qqplot')
    plt.tight_layout()
    plt.savefig("../figs/data_qqplot.png")

if __name__=="__main__":
    
    data= [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
    
    print_frequencies(data)
    save_boxplot(data)
    save_histogram(data)
    save_qqplot(data)