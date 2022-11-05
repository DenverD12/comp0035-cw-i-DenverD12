import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt ##  need to explain each one why imported after and remove any unused

from pathlib import Path

def open_data():
    
    
   
    return df

def process_data():
    """
    Loads data given filepath using pathlib and processes data
    
    Args:
        data: Pandas dataframe of the Tourism data

    Returns:
        df_arrivals: a prepared dataframe on the arrivals dataset
    """
    Tourism_arrivals_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_arrivals.csv')
    # Load first dataset with arrival data, 3 rows skip as first 3 rows contain logo, irrelevant info and blank row, in a new dataframe
    df_arrivals = pd.read_csv(Tourism_arrivals_csv, skiprows=3)
    
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_arrivals.shape[0] + 1)
    pd.set_option('display.max_columns', df_arrivals.shape[1] + 1)

    return df_arrivals

def prepare_data():
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the Tourism data set for number of arrivals for each country over different years.

    Args:
        data: Pandas dataframe of the Tourism data

    Returns:
        df_arrivals: a prepared dataframe on the arrivals dataset
    """
    
    df_arrivals = process_data()

    # Print number of columns and rows
    print("\nShape\n", df_arrivals.shape) 

    # Print the first 5 rows
    print("\nHead - first 5 rows\n", df_arrivals.head(5))

    # Print details about the rows and columns, including data types
    print("\nInfo\n", df_arrivals.info(verbose=True)) 

    

    

    


    return df_arrivals
   
    
    
if __name__ == '__main__':
    ''' 

    '''
    process_data()
    prepare_data()
    

    
    
    
    

    