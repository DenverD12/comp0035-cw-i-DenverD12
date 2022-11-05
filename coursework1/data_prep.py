import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt ##  need to explain each one why imported after and remove any unused

from pathlib import Path


def load_data():
    """
    Loads data given filepath using pathlib and processes data
    
    Args:
        data: Pandas dataframe of the Tourism data

    Returns:
        df_arrivals: a prepared dataframe on the arrivals dataset
    """
    Tourism_arrivals_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_arrivals.csv')
    # Load first dataset with arrival data, skips 3 rows as first 3 rows contain logo, irrelevant info and blank row, in a new dataframe
    df_arrivals = pd.read_csv(Tourism_arrivals_csv, skiprows=3)
    
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_arrivals.shape[0] + 1)
    pd.set_option('display.max_columns', df_arrivals.shape[1] + 1)

    return df_arrivals

def explore_data_arrivals():
    """
    Explores the Tourism data set for number of arrivals for each country 
    over different years.
    Args:
        data: Pandas dataframe of the Tourism data
    Returns:
        df_arrivals: a prepared dataframe on the arrivals dataset
    """
    df_arrivals = load_data()
    # Print number of columns and rows
    print("\nShape\n", df_arrivals.shape) 
    # Print the first 5 rows
    print("\nHead - first 5 rows\n", df_arrivals.head(5))
    # Print the last 5 rows
    print("\nTail - last 5 rows\n", df_arrivals.tail(5))

    # Print unique values in "Indicator Name" and 'Indicator code' columns
    print("\nUnique values - 'Indicator Name' col\n", df_arrivals['Indicator Name'].unique())
    print("\nUnique values - 'Indicator Code' \n", df_arrivals['Indicator Code'].unique())

    # Print details about the rows and columns, including data types
    print("\nInfo - arrivals\n", df_arrivals.info(verbose=True)) 
    return df_arrivals

def drop_columns_arrivals():
    
    df_arrivals = explore_data_arrivals()
    # Drop empty columns (36 year columns and 1 blank)
    df_arrivals.dropna(how='all', axis=1, inplace=True)
    # Drops 'Indicator Code' column as same info as 'Indicator Name' column
    df_arrivals.drop(['Indicator Code'], axis=1, inplace=True)

    

    return df_arrivals

def load_data_metadata():

    # Open 'metadata.csv' dataset - has country income level and regions
    metadata_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'metadata.csv')
    # Opens dataset with income group and region, no rows skipped, all relevant, in a new dataframe 
    df_income_regions = pd.read_csv(metadata_csv)
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_income_regions.shape[0] + 1)
    pd.set_option('display.max_columns', df_income_regions.shape[1] + 1)  

    return df_income_regions

def prepare_data_metadata():

    df_income_regions = load_data_metadata()
    df_arrivals = drop_columns_arrivals()
    # Print details about the rows and columns, including data types
    print("\nInfo - metadata\n", df_income_regions.info(verbose=True)) 

    # Drop the 'SpecialNotes' column (unnecessary as just description)
    df_income_regions.drop(['SpecialNotes'], axis=1, inplace=True)

    # Drop the 'TableName' column (same as 'Country Name' column in original)
    df_income_regions.drop(['TableName'], axis=1, inplace=True)

    # Drop the null empty column at the end
    df_income_regions.dropna(how='all', axis=1, inplace=True)

    # Print details about the rows and columns, including data types
    print("\nInfo - metadata\n", df_income_regions.info(verbose=True)) 
    
    # Merge the columns where df['Country Code'] matches df_income_regions['Country Code']
    df_merged = df_arrivals.merge(df_income_regions, how='right', left_on='Country Code', right_on='Country Code')
    print("\nInfo\n", df_merged.info(verbose=True)) 
    
    # Moving end columns to third and fourth position 
    # Pop each column and add each to a variables
    Region_column = df_merged.pop('Region')
    Income_column = df_merged.pop('IncomeGroup')
    
    # Insert each varaible to correct position
    df_merged.insert(2, Region_column.name, Region_column)
    df_merged.insert(3, Income_column.name, Income_column)

    
    print("\nInfo\n", df_merged.info(verbose=True)) 
    

    return df_arrivals, df_merged
   
    
    
if __name__ == '__main__':
    ''' 
    
    '''
    load_data()
    explore_data_arrivals()
    drop_columns_arrivals()
    load_data_metadata()
    prepare_data_metadata()

    

    
    
    
    

    