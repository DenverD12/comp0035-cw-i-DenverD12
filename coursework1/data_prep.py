import numpy as np 
import pandas as pd
import seaborn as sns ##pip install seaborn mention in readme.
import matplotlib.pyplot as plt ##  need to explain each one why imported after and remove any unused

from pathlib import Path


def load_data_arrivals():
    """
    Loads data given filepath using pathlib and processes data 
    as a pandas dataframe
    
    Args:
        None
    Returns:
        df_arrivals: a pandas dataframe on the arrivals.csv dataset
    """   
    # Load arrivals.csv in a new dataframe, skips 4 rows
    arrivals_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data',
                                                        'arrivals.csv')
    df_arrivals = pd.read_csv(arrivals_csv, skiprows=4)
    
    # Set pandas display options to no. of columns and rows in dataframe
    pd.set_option('display.max_rows', df_arrivals.shape[0] + 1)
    pd.set_option('display.max_columns', df_arrivals.shape[1] + 1)

    return df_arrivals


def basic_visualise_data(data):
    """
    Displays shape, first 5 rows, last 5 rows and column details
    
    Args:
        data: any dataset as pandas dataframe
    Returns: 
        Prints of shape, head, tail and other column info
    """
    # Print number of columns and rows
    print("\nShape\n", data.shape) 
    # Print the first 5 rows
    print("\nHead - first 5 rows\n", data.head(5))
    # Print the last 5 rows
    print("\nTail - last 5 rows\n", data.tail(5))
    
    # Print details about the rows and columns, including data types
    print("Info", data.info(verbose=True)) 
    return data


def visual_chart_missing_values(data):
    # Adapted from code written by datavizpyr website
    # https://datavizpyr.com/visualizing-missing-data-with-seaborn-heatmap-and-displot/
    """
    This function plots a bar chart that visualises 
    the missing values for each column.
    The orange areas represent missing values 
    and the 'Count' x axis represents the missing value count
    
    Args:
        data: pandas dataframe of any dataset in this case arrivals.csv
    Returns:
        None 
    """
    # Creates a plot with height and aspect ratio to show data clearly
    sns.displot(data = df_arrivals.isna().melt(value_name="missing"), 
                                               y="variable", hue="missing",
                                               multiple="fill", height=10, 
                                               aspect=1)
    # Saves plot figure in 'data' folder in coursework1 repository
    plt.savefig("Visualisation of missing data in columns of the dataset arrivals.csv.png", dpi=100)


def explore_data_arrivals(data):
    """
    Explores the arrivals data set for number of arrivals for each country 
    over different years.

    Args:
        data: Pandas dataframe of the Tourism data
    Returns:
        df_arrivals: a prepared dataframe on the arrivals dataset
    """
    df_arrivals = data
    # Run basic visualiations function defined before
    basic_visualise_data(df_arrivals)
    # Run function to plot a seaborn chart for missing values
    visual_chart_missing_values(df_arrivals)

    # Print unique values in first 4 columns
    print("\nUnique values - 'Country Name' col\n",
          df_arrivals['Country Name'].unique())
    print("\nUnique values - 'Country Code' col\n", 
          df_arrivals['Country Code'].unique())
    print("\nUnique values - 'Indicator Name' col\n", 
          df_arrivals['Indicator Name'].unique())
    print("\nUnique values - 'Indicator Code' \n", 
          df_arrivals['Indicator Code'].unique())
    
    return df_arrivals


def drop_year_columns_arrivals(): 
    """
    Drops fully empty year columns and 'Indicator Code' column

    Args:
        None
    Returns:
        dataframe with dropped columns     
    """
    df_arrivals = load_data_arrivals()
    # Drop empty columns (36 year columns and 1 blank)
    df_arrivals = df_arrivals.dropna(how='all', axis=1)
    # Drop 'Indicator Code' column
    df_arrivals = df_arrivals.drop(['Indicator Code'], axis=1)

    return df_arrivals


def load_data_metadata():
    """
    Loads data given filepath using pathlib and processes data 
    as a pandas dataframe

    Args:
        None
    Returns:
        df_ametadata: a pandas dataframe on the metadata.csv dataset
    """
    # Open 'metadata.csv' dataset - has country income level and regions
    metadata_csv = Path(__file__).parent.parent.joinpath(
        'coursework1', 'data','metadata.csv',
        )
    # Opens dataset with income group and region with no rows skipped
    df_metadata = pd.read_csv(metadata_csv, skiprows=0)
    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df_metadata.shape[0] + 1)
    pd.set_option('display.max_columns', df_metadata.shape[1] + 1)  

    return df_metadata


def drop_columns_metadata():
    """
    Drops three columns: 'SpecialNotes', 'TableName' and null column
    from metadata.csv pandas dataframe

    Args:
        None
    Returns:
        df_metadata: metadata.csv dataframe
        with mentioned columns dropped
    """
    # Load metadata.csv to a dataframe using helper function
    df_metadata = load_data_metadata()
    # Run basic visualisations (defined in original function)
    basic_visualise_data(df_metadata)
   
    # Drop the 'SpecialNotes', 'TableName' columns
    df_metadata = df_metadata.drop(['SpecialNotes'], axis=1)
    df_metadata = df_metadata.drop(['TableName'], axis=1)
    # Drop the fully trailing empty null column
    df_metadata = df_metadata.dropna(how='all', axis=1)

    # Reassigned dataframe with new name with better clariy of contents
    df_income_regions = df_metadata

    return df_income_regions


def merge_arrivals_metadata(data1, data2):
    """
    Merges arrivals.csv and metadata.csv pandas dataframes
    using common column

    Args:
        data1: pandas dataframe of arrivals.csv
        data2: pandas dataframe of metadata.csv
    Returns:
        df_merged: merged dataframe of arrivals.csv and metadata.csv
    """
    df_arrivals = data1
    df_income_regions = data2

    # Print unique values in 'Country Code' column
    print("\nUnique values - 'Country Code' in metadata.csv\n", 
          df_income_regions['Country Code'].unique())
   
    # Merge columns where df['Country Code'] match df_income_regions['Country Code']
    df_merged = df_arrivals.merge(df_income_regions, how='right', 
                                  left_on='Country Code', 
                                  right_on='Country Code')
    # Drop the 'Country Code' column
    df_merged = df_merged.drop(['Country Code'], axis=1)
    

    return df_merged


def reorder_columns(data):
    """
    Reorders the end columns 'Region' and 'IncomeGroup' to position
    with index 1 and 2

    Args:
        data: pandas dataframe of the merged datasets
    Returns:
        df_merged: merged dataframe with columns reordered
    """
    df_merged = data
   
    # Pop each column and add each to a variable
    Region_column = df_merged.pop('Region')
    Income_column = df_merged.pop('IncomeGroup')
    # Insert each variable to correct third and fourth position
    df_merged.insert(1, Region_column.name, Region_column)
    df_merged.insert(2, Income_column.name, Income_column)
    
     # Print list of column names in new order
    print("\nMerged data - columns reordered check\n", 
          list(df_merged.columns.values)) 

    return df_merged



def make_list_country_names():
    """
    Helper function: A variable holding a list is created from 
    officially recognised country names to check for inconsistencies

    Args:
        None
    Returns:
        df_country_names_worldbank: a pandas dataframe of 
                                    the country_names.csv dataset
    """
    
    # Define list with officially recognised country names 
    country_names_worldbank  = [ 
        "Afghanistan", "Albania", "Algeria", "American Samoa", 
        "Andorra", "Angola", "Antigua and Barbuda", "Argentina", 
        "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", 
        "Bahamas, The", "Bahrain", "Bangladesh", "Barbados", 
        "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", 
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
        "British Virgin Islands", "Brunei Darussalam", "Bulgaria", 
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
        "Canada", "Cayman Islands", "Central African Republic", "Chad", 
        "Channel Islands", "Chile", "China", "Colombia", "Comoros",
        "Congo, Dem. Rep.", "Congo, Rep.", "Costa Rica", "Cote d'Ivoire", 
        "Croatia","Cuba", "Curacao", "Cyprus", "Czechia", "Denmark", 
        "Djibouti","Dominica", "Dominican Republic", "Ecuador", 
        "Egypt, Arab Rep.", "El Salvador", "Equatorial Guinea", "Eritrea", 
        "Estonia", "Eswatini", "Ethiopia", "Faroe Islands", "Fiji", 
        "Finland", "France", "French Polynesia", "Gabon", "Gambia, The", 
        "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", 
        "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
        "Haiti", "Honduras", "Hong Kong SAR, China", "Hungary", "Iceland", 
        "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Ireland", 
        "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
        "Kazakhstan", "Kenya", "Kiribati", "Korea, Dem. People's Rep.", 
        "Korea, Rep.", "Kosovo", "Kuwait", "Kyrgyz Republic", "Lao PDR", 
        "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
        "Lithuania", "Luxembourg", "Macao SAR, China", "Madagascar", "Malawi",
        "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
        "Mauritania", "Mauritius", "Mexico", "Micronesia, Fed. Sts.", 
        "Moldova","Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", 
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", 
        "New Caledonia", "New Zealand", "Nicaragua", "Niger", 
        "Nigeria", "North Macedonia", "Northern Mariana Islands", 
        "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
        "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
        "Puerto Rico", "Qatar", "Romania", "Russian Federation", 
        "Rwanda", "Samoa", "San Marino", "Sao Tome and Principe", 
        "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", 
        "Singapore", "Sint Maarten (Dutch part)", "Slovak Republic", 
        "Slovenia", "Solomon Islands", "Somalia", "South Africa", 
        "South Sudan", "Spain", "Sri Lanka", "St. Kitts and Nevis", 
        "St. Lucia", "St. Martin (French part)", 
        "St. Vincent and the Grenadines", "Sudan", "Suriname", "Sweden", 
        "Switzerland", "Syrian Arab Republic", "Tajikistan", "Tanzania", 
        "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", 
        "Tunisia", "Turkiye", "Turkmenistan", "Turks and Caicos Islands", 
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", 
        "United Kingdom", "United States", "Uruguay", "Uzbekistan", 
        "Vanuatu", "Venezuela, RB", "Vietnam", "Virgin Islands (U.S.)", 
        "West Bank and Gaza", "Yemen, Rep.", "Zambia", "Zimbabwe"
        ]

    return country_names_worldbank


def country_names_clean(data):
    """
    Checks in the 'Country Names' column for inconsistencies,
    unnecessary rows and removes country groupings 
    
    Args:
        data1: pandas dataframe of merged datasets
        data2: list containing officially recognised country names
    Returns:
        df_merged: pandas merged dataframe after unneeded rows dropped
    """
    df_merged = data
    # Print unique values in "Country Name" column
    print("\nUnique values - 'Country Name' col\n", 
          df_merged['Country Name'].unique())

    # Assign the list from the make_list_country_names() function:
    country_names_worldbank = make_list_country_names()

    # (The below code was adapted from: 
    # https://www.interviewqs.com/ddi-code-snippets/rows-cols-python)
    # Print the rows that don't match country_names_list
    print ("\nRows without World Bank defined countries \n", 
           df_merged.loc[~df_merged['Country Name']
            .isin(country_names_worldbank)])
    
    # Drops all rows with values not in "country_names_list" 
    df_merged = df_merged[df_merged['Country Name'].isin(country_names_worldbank)]
  
    # Print head, shape after droping country group rows
    print("\nHead after country group rows drop\n", df_merged.head())
    print("\nShape after country group rows drop\n", df_merged.shape)

    return df_merged

    

def empty_rows_check(data):
    """
    Checks for & displays empty rows and rows with over 50% null values
    in the merged dataframe df_merged
    
    Args:
        data: the merged panda datafram df_merged 
    Returns: 
        df_merged: merged pandas dataframe unaltered
    """
    df_merged = data
    
    # Count the number of rows where all the columns are empty (null)
    print("\nNumber of rows where all columns are empty\n", 
          df_merged.isna().all(axis=1).sum())
  
    # Print details about rows and columns, including data types
    print("Column information - merged\n", 
          df_merged.info(verbose=True)) 
  
    # Display row with 1 null in 'IncomeGroup' column:
    print("\nRow with null value in 'IncomeGroup'column:\n", 
          df_merged[df_merged["IncomeGroup"].isnull()])
  
    # Amount of columns excluding the 5 full information columns 
    amount_columns = len(df_merged.axes[1])
    
    # Print rows % of missing values
    print("\nColumns showing initial % of missing values\n", 
         (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))

    # Variable with 50% of no. of columns defined
    count_50_percent = 0.5 * amount_columns
  
    # Display number of rows with null values greater than 50%
    print("\nNo. of rows with >50% of missing values\n", 
         (df_merged.isnull().sum(axis=1) > count_50_percent).sum())
    # Display info on which rows have null values greater than 50%
    print("\nInfo of rows with >50% of missing values\n", 
          df_merged.isnull().sum(axis=1) > count_50_percent)
    # Print some flagged >50% null rows
    print("\nSome Rows with >50% missing values\n",
          df_merged.loc[[2, 8, 38, 220]])
 
    return df_merged
    
def drop_empty_rows(data):
    """
    Drops rows with over 50% of missing data
    
    Args:
        data: the merged pandas dataframe df_merged 
    Returns: 
        df_merged: merged pandas dataframe after dropped rows 
        containing over 50% nulls
    """
    
    df_merged = data
    # Redefine variable of 50% count from previous function
    amount_columns = len(df_merged.axes[1])
    count_50_percent = 0.5 * amount_columns

    # Drops rows over 50% empty
    df_merged = df_merged.dropna(thresh=count_50_percent, axis=0)

    # Print number of rows and columns after removal
    print("\nShape after >50% null removal\n", df_merged.shape) 
    # Print the columns showing the % of missing values
    print("\nColumns showing % of missing values after 50% null removal\n",
         (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))
   
    return df_merged
   
def unique_values_check_remaining_columns(data):
    """
    Checks for duplicates and unique values of the first 4 columns
    
    Args:
        data: the merged pandas dataframe df_merged 
    Returns:
        df_merged: the merged pandas dataframe unaltered 
    """
    
    df_merged = data

    # Print no. of duplicates in 'Country Name', 'Country Code' columns
    print("\nDuplicates in 'Country Name'?\n", 
          df_merged.duplicated(subset=['Country Name']).any().sum())

    # Print unique values in "Region", "IncomeGroup", "Country Name" columns
    print("\nUnique values - 'Region' column\n", df_merged['Region'].unique())
    print("\nUnique values - 'IncomeGroup' column\n", 
          df_merged['IncomeGroup'].unique())
    print("\nUnique values - 'Country Name' column\n", 
          df_merged['Country Name'].unique()) 
    
    return df_merged

    
def clean_names_country_names_column(data):
    """
    Renames certain inconsistent values in the "Country Name" column 
    with a more clear and useful format
    
    Args:
        data: the merged pandas dataframe df_merged 
    Returns:
        ds_merged: the merged dataframe after renaming
    """
    
    # Replaces values in 'Country Name' column:
    # Replaces 'Bahamas, The' with 'The Bahamas'
    # Replaces 'Gambia, The' with 'The Gambia'
    data = data["Country Name"].replace(["Bahamas, The", "Gambia, The"],
                                        ["The Bahamas", "The Gambia"])

    return df_merged


def check_basic_stats(data):
    """
    Checks basic statistics for each year column 
    Shows count, mean, standard deviation (std), lower(25%) 
    and upper(75%) quartiles, median(50%) and maximum values
    
    Args:
        data: pandas dataframe of merged dataset
    Returns:
        df_merged: unaltered pandas merged dataframe
    """
    df_merged = data

    pd.set_option('display.max_rows', df_merged.shape[0] + 1)
    pd.set_option('display.max_columns', df_merged.shape[1] + 1)

    print("\nBasic stats for df_merged dataframe year columns:\n", 
          df_merged.describe())

    return df_merged



if __name__ == '__main__':
    ''' 
    Main function that runs every other function
    '''
    # Set all columns visible in terminal
    pd.set_option('display.max_columns', None)

    # Load arrivals.csv using function
    df_arrivals = load_data_arrivals()
    explore_data_arrivals(df_arrivals)

    # dataframe after dropping columns for arrivals.csv and metadata.csv
    df_arrivals_dropped_cols = drop_year_columns_arrivals()
    df_income_regions_drop_cols = drop_columns_metadata()
    
    # dataframe after merging arrivals.csv and metadata.csv datasets
    df_merged = merge_arrivals_metadata(
        df_arrivals_dropped_cols, df_income_regions_drop_cols)
    df_columns_reordered = reorder_columns(df_merged)
    df_merged_cleaned_1st_column = country_names_clean(df_merged)

    df_merged = empty_rows_check(df_merged_cleaned_1st_column)
    df_50_percent_nulls_drop = drop_empty_rows(df_merged)
    df_merged_unique_check = \
        unique_values_check_remaining_columns(df_50_percent_nulls_drop)

    df_merged_clean_countrynames = \
        clean_names_country_names_column(df_merged_unique_check)
    
    df_merged_prepared = check_basic_stats(df_merged_clean_countrynames)
    
    # The below was code used to export the final csv file
    # prepared_csv_filepath = Path(__file__).parent.parent.joinpath(
    #    'coursework1', 'data', 'Tourism_arrivals_prepared.csv')
    # df_merged_final.to_csv(prepared_csv_filepath, index=False)
    
