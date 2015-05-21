
def load_data(url):
    df = pd.read_csv(url)
    df.dropna(inplace=True)
    return df

def save_plots(df, column):
    f,ax=plt.subplots()
    df.boxplot(column=column, ax=ax)
    plt.savefig("../figs/lending_boxplot")
    f,ax=plt.subplots()
    df[column].hist(ax=ax, bins=30)
    plt.savefig("../figs/lending_histogram")
    f,ax=plt.subplots()
    _=scipy.stats.probplot(df[column].values, dist="norm", plot=plt)
    plt.savefig("../figs/lending_qqplot")
    
if __name__=="__main__":
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy.stats
    
    dataurl='https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv'
    df=load_data(dataurl)
    save_plots(df, "Amount.Requested")
