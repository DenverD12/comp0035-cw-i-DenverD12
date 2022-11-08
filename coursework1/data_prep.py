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
    sns.displot(data = df_arrivals.isna().melt(value_name="missing"), 
                                               y="variable", hue="missing",
                                               multiple="fill", height=10, 
                                               aspect=1.25)

    plt.savefig("Visualisation of missing data in columns of the dataset arrivals.csv.png", dpi=100)
    plt.show()

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
    ##The 'Country Code' column unique values was displayed for the metadata.csv dataset as this column name is common to both arrivals.csv and metadata.csv datasets.
    ##After inspecting the output, it can be seen the country codes in metadata.csv are identical to 'arrivals.csv' found in a previous section. Therefore, this column will be used as a common column to merge boht sets.

    ##Now the two datasets 'arrivals.csv" and "metadata.csv will be merged in order that the income group and regions are shown with the number of arrivals. These two columns of information will be useufl to group the country types later for analysis. They are also mentioned in the problem statement and questions which refer to these two variables.
    ##Common columns to both datasets were 'Country Code', so this is what is used to merge via common column values.
    # Merge columns where df['Country Code'] match df_income_regions['Country Code']
    df_merged = df_arrivals.merge(df_income_regions, how='right', 
                                  left_on='Country Code', 
                                  right_on='Country Code')
    print("\nInfo\n", df_merged.info(verbose=True)) 

    return df_merged

def reorder_columns(data):
    """
    Reorders the end columns 'Region' and 'IncomeGroup' to position
    with index 2 and 3

    Args:
        data: pandas dataframe of the merged datasets
    Returns:
        df_merged: merged dataframe with columns reordered
    """
    df_merged = data
    ##The two remaining uncommon columns in the "metadata.csv" dataset called 'Region' and 'IncomeGroup' are initially moved to the end of the merged dataset upon merging which is disadvantageous since they are information columns so they would be more useful to be near the start with other columns. These will need to be moved near to the left side of the merged dataset. It was chosen to move it in from of 'Country Code' and just before 'Indicator Name' so it is evident that the data in the following columns clearly represent the number of arrivals.
    ##Moving end columns to third and fourth position 
    # Pop each column and add each to a variable
    Region_column = df_merged.pop('Region')
    Income_column = df_merged.pop('IncomeGroup')
    ##columns were each popped using `.pop` (i.e. removed and returned for use in the next functions) in order to insert them back in the correct position with `.insert`
    # Insert each variable to correct third and fourth position
    df_merged.insert(2, Region_column.name, Region_column)
    df_merged.insert(3, Income_column.name, Income_column)

    ##A check was carried out to check if columns were now in correct position by displaying the column names in order. The order was observed to be correct since 'Region' and 'IncomeGroup' were listed just after 'Country Code' and before 'Indicator Name'. 
    # Print details about the rows and columns, including data types
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
        df_country_names_worldban: a pandas dataframe on the country_names.csv dataset
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

def country_names_clean(data1, data2):
    """
    Checks in the 'Country Names' column for inconsitencies and
    unneccessary rows, particularly country groups by matching with 
    a list of officially recognised names
    Args:
        data1: pandas dataframe of merged datasets
        data2: list containing offically recognised country names
    Returns:
        df_merged: pandas merged dataframe after unneeded rows dropped
    """
    df_merged = data1
    # Print unique values in "Country Name" column
    print("\nUnique values - 'Country Name' col\n", 
          df_merged['Country Name'].unique())

    ## After observing the unique values in the 'Country Names' column, some unsual country names can be seen. For example, 'IDA blend'. Upon researching this, it was found this is a group of countries, which all are already individually listed as separate values in the dataset 'Country Name' column. For example 'Chad' is visible. 
    ## According the the World Bank website, which is the same as the dataset, the officially recognised contries in the contents which are used in every dataset were found at https://data.worldbank.org/country.
    ## Although external datasets were not allowed to be used, since the countries in that countries page are the exact same ones they use on every dataset, it was safe to assume at this point that they could be all included in the current used dataset arrivals.csv. This assumption can be validated later.
    ## A list containing the offical country names was simply created by copying and pasting the names from the website list as code, then wrapping each in quotations. Then, by highlighting and using the command Join Lines from the VSCode commands, they were all fit onto lines within the 80 character limit. Leading and trailing whitespaces were carefully checked to confirm they weren't present to prevent further inconsistencies. 
    ##The reasoning behind this is to later see which values in 'Country Name' column matcht. The ones that don't match will most likely be the groupings and will be displayed later to help make a decision on whether to remove them.
    ## This method also ensures perfect format as no whitespaces, special characters or spelling errors are present.
    
    # Assign the list from the make_list_country_names() function:
    country_names_worldbank = data2

    ## reference https://www.interviewqs.com/ddi-code-snippets/rows-cols-python
    # Print the rows that don't match country_names_list
    print ("\nRows without World Bank defined countries \n", 
        df_merged.loc[~df_merged['Country Name'].isin(country_names_worldbank)])
    
    ##https://stackoverflow.com/questions/27965295/dropping-rows-from-dataframe-based-on-a-not-in-condition
    ##From the displayed rows, there are country groupings such as the 'IDA blend' etc. which will not be of any use to the target audience or problem statement. The target audience is looking for specific countries to set up their hotel. Some values such as 'Middle East & North Africa' represent the regions and others like 'Low income' represent the income group which both do relate to the problem statement and business need. However, since there is a separate column for both of these categories (which is 'Region' and 'IncomeGroup' respectively), these rows will also not be removed from the 'Country Name' column.
    ##Another detail that can be observed is the fact that every value here is a group of countries clearly validates the assumption on the country lists made earlier.
    # Drops all rows with values not in "country_names_list" 
    df_merged = df_merged[df_merged['Country Name'].isin(country_names_worldbank)]
    
    ##Therefore due to the above reasons, any rows containing values in the 'Country Name' column which are not part of the 217 officially recognised countries are dropped (removed) from the dataset. 
    
    ##After the dropped rows, to check if it worked as expected, the head (the first 5 rows), and the shape is displayed. The head shows in particular the rows with value 'Africa Eastern and Southern' and 'Africa Western and Central' have been successfuly removed.
    ##The shape shows 217 rows which matched the number of offically recognised countries in the World Data Bank (217) so this step was successful.
    # Print head, shape after droping country group rows
    print("\nHead after country group rows drop\n", df_merged.head())
    print("\nShape after country group rows drop\n", df_merged.shape)

    return df_merged

def missing_values_chart(data):
    df_merged = data
    
    

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
    ##To begin with removing rows with null values, first fully empty rows were checked and counted. The total came back with 0 meaning all rows contained some data.
    
    ## Column details and info were viewed again to see which columns were completely full.  3 columns ('Country Name', 'Country Code' and 'Indicator Name') were completely full with no null values.
    # Print details about rows and columns, including data types
    print("Column information - merged\n", 
          df_merged.info(verbose=True)) 
    ## The 'IncomeGroup' shows 216 non-null values meaning 1 value on that column is null so this will be investigated.

    # Display row with 1 null in 'IncomeGroup' column:
    print("\nRow with null value in 'IncomeGroup'column:\n", 
          df_merged[df_merged["IncomeGroup"].isnull()])
    ##The row displayed was Venezuala. After doing some research in order to do an imputation of the missing value, it was found that Venezuela is officially unclassified in its income level. Therefore, for this columm and value, nothing can be done and is left blank. Reference: https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2021-2022 

    ## A variable "amount_columms" is defined which holds a count of the number of columns for use in printing rows with a percentage of empty values. 
    # Amount of columns excluding the 5 full information columns 
    amount_columns = len(df_merged.axes[1])
    
    # Print rows % of missing values
    print("\nColumns showing % of missing values\n", 
         (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))
    ##The percentage of missing (null) values was displayed to get an idea of the proportion of the rows that were empty. Some rows, like rows with index, had a large percentage of missing values at around 83% for example. These high percentages will be removed but first a lower threshold to the allowed maximum percentage is defined in the next step.
    
    # Variable with 50% of no. of columns defined
    count_50_percent = 0.5 * amount_columns
    ##A lower threshold of 50% of the number of columns is defined the then see which rows have more than 50% data missing. The reasoning behind this chosen percentage is as follows: If 50% of columns allowed then, 50% of the no. of columns in this dataset (31) = 15.5. Since the first 5 columns have no null values and are not the years columns, taking this away from 31 = 26 year columns. 26 - 15.5 = 10.5 meaning there is approximately at least 10 years of data remaining as the minimum. 10 years, i.e. 10 non-null values in the row is deemed sufficient span of years to compute calculations in later steps as well as in the next coursework.
    
    ## The number of rows with over 50% null values were counted and 22 were found. Then a true or false boolean indicated which specific rows they were. 
    ##A display of the number of rows with number of null balues greater than 50% found 22 rows.
    # Display number of rows with null values greater than 50%
    print("\nNo. of rows with 50% of missing values\n", 
         (df_merged.isnull().sum(axis=1) > count_50_percent).sum())
    # Display info on which rows have null values greater than 50%
    print("\nInfo of rows with 50% of missing values\n", 
          df_merged.isnull().sum(axis=1) > count_50_percent)
    
    
    # Print some flagged empty rows
    print("\nSome Rows with 50% missing values\n",
          df_merged.loc[[2, 8, 38, 220]])
    ##Some of the rows that were 50% empty were observed to help make a better decision on the missing values. 
    ##After doing some research on World Bank Data website, and on the internet, for the missing rows, no data could be found for number of arrivals for these countries. For example for 'Afghanistan', it can be seen there is no data available on World Bank Data: https://data.worldbank.org/indicator/ST.INT.ARVL?locations=AF. 
    ##If later averages and calulations need to be done, countries with more than 50% of missing data will not be useful or accurate to represent countries over the large time scale of years. 
    ##Therefore, due to the above reasons, these country rows were decided to be dropped. 
    return df_merged
    
def drop_empty_rows(data):
    """
    Drops rows with over 50% of missing data
    Args:
        data: the merged pandas dataframe df_merged 
    Returns: 
        df_merged: merged pandas dataframe after dropped rows 
        containg over 50% nulls
    """
    df_merged = data
    # Redefine variable of 50% count from previous function
    amount_columns = len(df_merged.axes[1])
    count_50_percent = 0.5 * amount_columns

    # Drops rows over 50% empty
    df_merged = df_merged.dropna(thresh=count_50_percent, axis=0)
    # Print number of rows and columns after removal
    print("\nShape after >50% null removal\n", df_merged.shape)
    ## For reasons outlined before, rows with over 50% null values are dropped. The shape is checked to see the number of rows is 185 after removal, which is 217-22 (defined previous step) which shows this step has been done successfully. 
    
    # Print the columns showing the % of missing values
    print("\nColumns showing % of missing values after 50% null removal\n",
         (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))
    ## The percentage of nulls in each row were then computed and displayed. Mostly the percentages have are very low by observation, and the higheest is 45% null values which is within the allowed amount so this further shows the data is ready in terms of null values. 
    
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

    ##First duplicates were checked for 'Country Name' and 'Country Code' column where a true or false statement was returned as these are the only columns where duplicates should not be present since each name and country code should be for each individual country. The results showed 'false' for both which is expected and confirmed no duplicates.
    
    # Print no. of duplicates in 'Country Name', 'Country Code' columns
    print("\nDuplicates in 'Country Name'?\n", 
          df_merged.duplicated(subset=['Country Name']).any().sum())
    print("Duplicates in 'Country Code'?\n", 
          df_merged.duplicated(subset=['Country Code']).any().sum())

    # Print unique values in "Region", "IncomeGroup", "Country Name" columns
    print("\nUnique values - 'Region' col\n", df_merged['Region'].unique())
    ## A check was done on the unique values in the 'Region' column to check for any inconsistencies. There are 7 regions printed, ['Latin America & Caribbean' 'Sub-Saharan Africa' 'Europe & Central Asia' 'East Asia & Pacific' 'South Asia' 'Middle East & North Africa' 'North America']. According to the World Bank Data website, the 7 regions match completely. https://data.worldbank.org/country
    ##This implies this column has no inconsitent values so nothing needs to be done for this column.

    print("\nUnique values - 'IncomeGroup' col\n", 
          df_merged['IncomeGroup'].unique())
    ##Another unique values check was done on the 'IncomeGroup' column for inconsistencies. The output printed 4 income groups: ['High income' 'Lower middle income' 'Upper middle income' 'Low income']. Again, doing a search on the World Bank Data website, these 4 regions match exactly, so there are no inconsitencies in this column. https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2022-2023#:~:text=The%20World%20Bank%20assigns%20the,the%20previous%20year%20(2021).
    ##It was taken into account that "Lower middle income" and "Higher middle income" are essentially just middle income but it was decided not to combine the two in order to match the official World Bank Data classifications.

    print("\nUnique values - 'Country Name' col\n", 
          df_merged['Country Name'].unique()) 
    ##A check was done on the 'Country Name' column again, this time to to check for any unneccesary words or orderings in names or parts that could possibly be slightly unclear to the user of the data.
    ##Most of the country names looked clear. However, there were 2 unclarities. For example, two countries 'Bahamas, The' and 'Gambia, The' could be written as 'The Bahamas' and 'The Gambia' for clarity which is their actual officially recognised country names. These 2 steps are addressed in the next step/function.
    
    ##Also the 'Indicator Name' code was analysed previously. It was found the one unique value was 'International Tourism, number of arrivals'. Although this is a long value name, it was decided to keep it unchanged due to the clear indication it gives of the type of data this is. For example, the international tourism indicates that the arrivals to the country are not from within the nation and strictly international. The 'number of arrivals' just makes it clear that the data represents number of people arriving in that country.
 
    return df_merged

    


def clean_names_country_names_column(data):
    """
    Renames certain values in the "Country Name" column with 
    a more useful format
    Args:
        data: the merged pandas dataframe df_merged 
    Returns:
        ds_merged: the merged dataframe after renaming
    """
    # Replace in 'Country Name' column:'Bahamas, The' with 'The Bahamas'
    # Replace 'Gambia, The' with 'The Gambia'
    data = data["Country Name"].replace("Bahamas, The", "The Bahamas")

    return df_merged

if __name__ == '__main__':
    ''' 
    Main function that runs every other function
    '''
    # Set all columns visible in terminal
    pd.set_option('display.max_columns', None)
    

    df_arrivals = load_data_arrivals()
    explore_data_arrivals(df_arrivals)

    df_arrivals_dropped_cols = drop_year_columns_arrivals()
    df_income_regions_drop_cols = drop_columns_metadata()
    

    df_merged = merge_arrivals_metadata(
        df_arrivals_dropped_cols, df_income_regions_drop_cols)
    df_columns_reordered = reorder_columns(df_merged)
    df_country_names_worldbank = make_list_country_names()
    
    df_merged_cleaned_1st_column = country_names_clean(df_merged, 
                                                       df_country_names_worldbank)

    df_merged = empty_rows_check(df_merged_cleaned_1st_column)
    df_50_percent_nulls_drop = drop_empty_rows(df_merged)
    df_merged_unique_check = unique_values_check_remaining_columns(df_50_percent_nulls_drop)

    df_merged_final = clean_names_country_names_column(df_merged_unique_check)
    
    # The below was code used to export the final csv file
    # prepared_csv_filepath = Path(__file__).parent.parent.joinpath(
    #    'coursework1', 'data', 'Tourism_arrivals_prepared.csv')
    # df_merged_final.to_csv(prepared_csv_filepath, index=False)
    
