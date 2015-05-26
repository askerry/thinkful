
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data(loansData):
    loansData['Interest.Rate']=loansData['Interest.Rate'].apply(lambda x: float(x[:-1]))
    loansData['Loan.Length']=loansData['Loan.Length'].apply(lambda x: float(x[:-7]))
    loansData['FICO.Score']=loansData['FICO.Range'].apply(lambda x: float(x.split('-')[0]))
    return loansData

def exploratory_viz(loansData):
    plt.figure()
    p = loansData['FICO.Score'].hist()
    plt.savefig('../figs/fico_score_hist.png')

    a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(14,14))
    plt.savefig('../figs/loan_scatter_matrix.png')

def extra_viz(loansData):
    f, ax = plt.subplots(figsize=(10, 10))
    sns.corrplot(loansData, ax=ax)
    plt.savefig('../figs/loan_corr_matrix.png')
    
def model(loansData, iv1, iv2, dv):    
    intrate = loansData[dv]
    fico = loansData[iv1]
    loanamt = loansData[iv2]

    # The dependent variable
    y = np.matrix(intrate).transpose()
    # The independent variables shaped as columns
    x1 = np.matrix(fico).transpose()
    x2 = np.matrix(loanamt).transpose()

    x = np.column_stack([x1,x2])

    X = sm.add_constant(x)
    model = sm.OLS(y,X)
    return model.fit()

def model2(loansData, iv1, iv2, dv):    
    for var in [iv1, iv2, dv]:
        loansData=loansData.rename(columns={var:''.join([char for char in var if char !='.'])})
    iv1=''.join([char for char in iv1 if char !='.'])
    iv2=''.join([char for char in iv2 if char !='.'])
    dv=''.join([char for char in dv if char !='.'])
    model = sm.OLS.from_formula('%s ~ %s + %s' %(dv, iv1, iv2), loansData)
    return model.fit()


if __name__=="__main__":
    loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
    loansData=clean_data(loansData)
    exploratory_viz(loansData)
    extra_viz(loansData)
    f=model2(loansData, 'FICO.Score', 'Amount.Requested', 'Interest.Rate')
    print f.summary()