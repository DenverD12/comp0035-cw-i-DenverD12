from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt # need to explain each one why imported after

def open_data():
    
    
   
    return df
    
def prepare_data(data):
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the Tourism data set for number of arrivals for each country over different years.

    Args:
        data: Pandas dataframe of the Tourism data

    Returns:
        df: Prints details about 
    """
    df = data

    # Print number of columns and rows
    print("\nShape\n", df.shape) 

    # Print the first 5 rows
    print("\nHead - first 5 rows\n", df.head(5))

    # Print details about the rows and columns, including data types
    print("\nInfo\n", df.info(verbose=True)) 

    # After above info results, 36 year columns are empty and 1 blank column at the end can be dropped
    df.dropna(how='all', axis=1, inplace=True)
    
    # Drop the 'Indicator Code' column as same info as 'Indicator Name' column
    df.drop(['Indicator Code'], axis=1, inplace=True)

    # Shows types for column data - we can see all data under year columns are floats ready for calculations so no need to convert
    print(df.dtypes)   

    # Merge dataset with the second dataset which shows country income level type
    Tourism_incometype_and_regions_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_incometype_and_regions.csv')
    # Opens dataset with income group and region, no rows skipped, all relevant, in a new dataframe 
    df_income_regions = pd.read_csv(Tourism_incometype_and_regions_csv)
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_income_regions.shape[0] + 1)
    pd.set_option('display.max_columns', df_income_regions.shape[1] + 1)  

    # Print details about the rows and columns, including data types
    print("\nInfo\n", df_income_regions.info(verbose=True)) 

    # Drop the 'SpecialNotes' column (unnecessary as just description)
    df_income_regions.drop(['SpecialNotes'], axis=1, inplace=True)

    # Drop the 'TableName' column (same as 'Country Name' column in original)
    df_income_regions.drop(['TableName'], axis=1, inplace=True)

    # Drop the null empty column at the end
    df_income_regions.dropna(how='all', axis=1, inplace=True)

    # Print details about the rows and columns, including data types
    print("\nInfo\n", df_income_regions.info(verbose=True)) 
    
    # Merge the columns where df['Country Code'] matches df_income_regions['Country Code']
    df_merged = df.merge(df_income_regions, how='right', left_on='Country Code', right_on='Country Code')
    print("\nInfo\n", df_merged.info(verbose=True)) 
    
    # Moving end columns to third and fourth position 
    # Pop each column and add each to a variables
    Region_column = df_merged.pop('Region')
    Income_column = df_merged.pop('IncomeGroup')
    
    # Insert each varaible to correct position
    df_merged.insert(2, Region_column.name, Region_column)
    df_merged.insert(3, Income_column.name, Income_column)

    
    
    # Preparing the third dataset on 'expenditures' before merge 
    # Import and read the 'expenditures' dataset
    expenditures_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'expenditures.csv')
    # Opens dataset with expenditures, no rows skipped, all relevant, in a new dataframe 
    df_expenditures = pd.read_csv(expenditures_csv, skiprows=4)
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_expenditures.shape[0] + 1)
    pd.set_option('display.max_columns', df_expenditures.shape[1] + 1)  

    # Print details about the rows and columns, including data types
    print("\nInfo\n", df_expenditures.info(verbose=True)) 
    
    # After above info results, 36 year columns are empty and 1 blank column at the end can be dropped
    df_expenditures.dropna(how='all', axis=1, inplace=True)

    # Drop the 'Indicator Code' column as same info as 'Indicator Name' column
    df_expenditures.drop(['Indicator Code'], axis=1, inplace=True)

    # Shows types for column data - we can see all data under year columns are floats ready for calculations so no need to convert
    print(df_expenditures.dtypes) 

    # Also drop 'Country Name' column as will be in new merged sheet (is in the df_merged dataframe)
    df_expenditures.drop(['Country Name'], axis=1, inplace=True)


    
    # Merge the columns where df_merged['Country Code'] matches df_expenditures['Country Code']
    df_prepared = df_merged.merge(df_expenditures, how='right', left_on='Country Code', right_on='Country Code')
    
    # Save the three datasets combined file ##Move later!!
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_prepared.csv')
    df_prepared.to_csv(prepared_csv_filepath, index=False)

    print("\nInfo\n", df_prepared.info(verbose=True)) 

    

    

    return df
   
    
    
if __name__ == '__main__':
    ''' 

    '''
    Tourism_arrivals_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_arrivals.csv')
    # Opens first dataset with arrival data, 3 rows skip as first 3 rows contain logo, irrelevant info and blank row, in a new dataframe
    df = pd.read_csv(Tourism_arrivals_csv, skiprows=3)
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)  

    
    
    prepare_data(df)
    

    