
import pandas as pd
from StringIO import StringIO
import sys
import exceptions
import numpy as np

def load_data(csvstring):
    '''load csv string into pandas dataframe'''
    return pd.read_csv(StringIO(csvstring))

def describe_center(df, substance):
    '''describe measures of central tendency for substance'''
    print "Measures of Central Tendency"
    print "The mean for {0} is {1:.2f}".format(substance, df[substance].mean())
    print "The median for {0} is {1:.2f}".format(substance, df[substance].median())
    mode=df[substance].mode()
    if len(mode)>0:
        mode=', '.join([str(val) for val in mode])
    else:
        mode="non-existent"
    print "The mode for {0} is {1}\n".format(substance, mode)
    
def describe_variability(df, substance):
    '''describe measures of variability for substance'''
    print "Measures of Variability"
    print "The range for {0} is {1:.2f}".format(substance, max(df[substance]) - min(df[substance]))
    print "The standard deviation for {0} is {1:.2f}".format(substance, df[substance].std())
    print "The variance for {0} is {1:.2f}\n".format(substance, df[substance].var())
    

if __name__=="__main__":
    
    csvstring = '''Region,Alcohol,Tobacco
    North, 6.47, 4.03
    Yorkshire, 6.13, 3.76
    Northeast, 6.19, 3.77
    East Midlands, 4.89, 3.34
    West Midlands, 5.63, 3.47
    East Anglia, 4.52, 2.92
    Southeast, 5.89, 3.20
    Southwest, 4.79, 2.71
    Wales, 5.27, 3.53
    Scotland, 6.08, 4.51
    Northern Ireland, 4.02, 4.56'''
    
    data=load_data(csvstring)
    columns=[col for col in data.columns if data[col].dtype==np.float64]

    if len(sys.argv)==1:
        substance=str(raw_input("Which substance: {}?\n".format(', '.join(columns))))
    else:
        substance=sys.argv[1]
    try:
        check=columns.index(substance)
    except exceptions.ValueError:
        check=None
        print "Substance not found in data set"
    if check is not None:
        describe_center(data, substance)
        describe_variability(data, substance)