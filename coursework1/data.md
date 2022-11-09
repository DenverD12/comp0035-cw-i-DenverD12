# **Data preparation and understanding**

# **Import required libraries**
```
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from pathlib import Path
```

# **Data Exploration of Tourism_arrivals.csv**

### **Loading arrivals.csv using a pandas data frame**
```
def load_data():

    Tourism_arrivals_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_arrivals.csv')
    df_arrivals = pd.read_csv(Tourism_arrivals_csv, skiprows=4)

    pd.set_option('display.max_rows', df_arrivals.shape[0] + 1)
    pd.set_option('display.max_columns', df_arrivals.shape[1] + 1)

    return df_arrivals
```
A function was created to load the Tourism_arrivals.csv dataset:
- The first line of written code in the function opens the file using the pathlib import so any OS user can access the path.  
- Four rows were skipped because the first row contained a logo and dataset title, the second and fourth row contained a blank row and the third row contained a 'Last Updated' date which was all unneeded for data preparation. 
- The last 2 written lines of code before the return statement were to set pandas display options to the number of columns and rows in the dataframe so all analysis can be viewed easily in the terminal.
<br/>
<br/>

### **explore_data_arrivals() function** ###
```
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

    basic_visualise_data(df_arrivals)
    visual_chart_missing_values(df_arrivals)

    print("\nUnique values - 'Country Name' col\n", df_arrivals['Country Name'].unique())
    print("\nUnique values - 'Country Code' col\n", df_arrivals['Country Code'].unique())
    print("\nUnique values - 'Indicator Name' col\n", df_arrivals['Indicator Name'].unique())
    print("\nUnique values - 'Indicator Code' \n", df_arrivals['Indicator Code'].unique())
    
    return df_arrivals
```
This function was made to explore the dataset.
<br/>

**Breaking down `explore_data_arrivals()` function:**
```
basic_visualise_data(df_arrivals)
```
This runs a helper function called `basic_visualise_data()` which is defined below:
### **basic_visualise_data() - Helper function** 
```
def basic_visualise_data(data):
    """
    Displays shape, first 5 rows, last 5 rows and column details
    
    Args:
        data: any dataset as pandas dataframe
    Returns: 
        Prints of shape, head, tail and other column info
    """
    print("\nShape\n", data.shape) 
    print("\nHead - first 5 rows\n", data.head(5))
    print("\nTail - last 5 rows\n", data.tail(5))
    
    print("Info", data.info(verbose=True)) 
    return data
```
**Breakdown of helper function:**
### **Number of rows and columns in Tourism_arrivals.csv**
```
print("\nShape\n", df_arrivals.shape)
```
### **Head - first 5 rows in Tourism_arrivals.csv**
```
print("\nHead - first 5 rows\n", df_arrivals.head(5))
```
From the first 5 rows, it can be seen that Tourism_arrivals.csv gives information about country names and country codes in the first 2 columns.  
The "Indicator Name" and "Indicator Code" column that represents that the overall data on the rows is for international number of arrivals of people in each country. 
The proceeding columns after seem to all be years and contain info on the number of arrivals for each country.  
<br/>

### **Tail - last 5 rows in Tourism_arrivals.csv**
```
print("\nTail - last 5 rows\n", df_arrivals.tail(5))
```
The last 5 rows were displayed to mostly see if the "Indicator Name" and "Indicator Code" contained the exact same values per column respectively and this held true so it could be possible to assume both whole columns may contain the same indicators throughout (per column).  
<br/>

### **Information on Rows and columns: column name, non-null count and dataypes**
```
print("Info", data.info(verbose=True)) 
```
A display of column names, non-null counts and datatype was carried out to understand the dataset more:  
- The first 4 columns ('Country Name', 'Country Code', 'Indicator Name' and 'Indicator Code') had a Dtype (datatype) of 'object' suggesting they were strings which meant these were worded columns that should be checked for unique values after.
- The first 4 columns were also non-null since they showed 266 which matched the shape earlier that showed row count of 266. This shows there was no missing values in them.
- The remaining columns seemed to be different years between 1960 and 2021 as well as an empty columns at the end represented by "Unnamed: 66" column name. They all had the datatype "flot 66" which indicated these contained float numbers. These values were the correct datatype to be used in calculations later on so no conversions were necessary.
- There were many columns with 0 non-nulls which indicate completely empty year columns. This could mean the year data for every country for number of international arrivals was missing for these years. A decision will later be made on what to do with these.
<br/>
<br/>

Returning to the next line in `explore_data_arrivals(data)` function:
```
visual_chart_missing_values(df_arrivals)
```
This runs a helper function defined below:

### **Seaborn bar chart function for missing data values:**
```
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
    sns.displot(data = df_arrivals.isna().melt(value_name="missing"), y="variable", hue="missing", multiple="fill", height=10,aspect=1.25)

    plt.savefig("Visualisation of missing data in columns of the dataset arrivals.csv.png", dpi=100)
```
The first line of code in this function creates a bar chart which helps to visualise the missing values in columns. The height was set to 10 so that the column names are more spaced out and easier to view.  
The chart figure is shown by clicking the link:
[Bar Chart showing distribution of missing values in columns](data/Visualisation%20of%20missing%20data%20in%20columns%20of%20the%20dataset%20arrivals.csv.png)
<br/>

From the barchart, the orange regions represent the missing (null) data and the blue represents the data that is not missing.
- This helps to further reinforce that the years 1960 to 1994 as well as 2021 have no data available for any countries since they are all orange bars which helps to understand those years do not have any data available and can be safely removed. Again, this could imply year data for every country for number of international arrivals was missing for these years so these columns are not useful.
- The last unnamed column, 'Unnamed: 66' is also completely orange indicating a unnecessary column which can be removed.
- Some useful information that can be seen which could not be seen previously with the `basic_visualise_data()` function is the trend in missing data for the year columns that aren't completely null. For example, the orange bar size gradually decreases as years progress from 1995 to 2007 indicating more data was made available overall for countries as time went on and missing data decreased.
- However, around the year 2017, the orange bar size gradually increased till 2020, indicating as time went on, the number of missing data values for arrivals increased.
- Therefore, this bar chart was a better method to understand the data.

 
<br/>

Now returning to the `explore_data_arrivals(data)` function:
## **Initial Unique values check on first 4 rows**
### **Unique values in 'Country Name' Column**
```
print("\nUnique values - 'Country Name' col\n", df_arrivals['Country Name'].unique())
```
### **Unique values in 'Country Code' Column**
```
print("\nUnique values - 'Country Code' col\n", df_arrivals['Country Code'].unique())
```  
### **Unique values in 'Indicator Name' Column**
```
print("\nUnique values - 'Indicator Name' col\n", df_arrivals['Indicator Name'].unique())
```
### **Unique values in 'Indicator Code' Column**
```
print("\nUnique values - 'Indicator Code' \n", df_arrivals['Indicator Code'].unique())
```
A unique values check was done on the first 4 rows since, from the information on column types earlier it could be seen in the 'Dtype' column that 
Initial Summary of unique values:
-  **'Country Name'** column: It appears to contain names of many countries. However, some groupings of countries seem to be present such as 'IDA blend' which, after research, was found to be a group of countries. This is unwanted as the main focus is for specific countries, then regions but most of these groups like 'IDA blend' are not countries or regions - this will be addressed and fixed in a later step.
- **'Country Code'** column: This appears to contain the country codes of each country.
- **'Indicator Name'** and **'Indicator Code'** columns: Previously, in the `basic_visualise_data()` function results for both the head and tail display, it was observed that 'Indicator Name' and 'Indicator Column' had the same values respectively throughout each. The unique value check test was done on both columns to verify the previous assumption that the whole column contained the same indicator throughout.  
The results show one unique value for both with 'International tourism, number of arrivals' and 'ST.INT.ARVL'. This not only proves the assumption, but also confirms there are no whitespaces or inconsistencies in these columns.  
- Both indicator columns are representing the same information so one column can be safely removed in later steps. Particularly, the 'ST.INT.ARVL' information is quite unclear so will be removed.
<br/>
<br/>

## **Drop columns in Tourism_arrivals.csv**
It was observed previously from the column details that columns (with index) 4 to 38 for years 1960 to 1994, as well as column 65 for year 2021 and 66 the unnamed end column, all contained completely empty values which was further seen on the bar chart. These were all year columns, except for the last column which was a completely blank column with no heading. This implied that there was no data on number of arrivals for those years at all. After doing some research, it could be concluded there was no data available for these years 1960 to 1994.  
Therefore, it is safe to make the decision to drop all these columns.  
For the year 2021, there was data available on the internet. However, for the purpose of this coursework, where ethical checks would need to be carried out to use this external data, it was decided to drop this column as well and just focus on the years provided.  
<br/>

The helper function was used:
### **drop_year_columns_arrivals() - Helper Function**
```
def drop_year_columns_arrivals(): 
    """
    Drops fully empty year columns and 'Indicator Code' column

    Args:
        None
    Returns:
        dataframe with dropped columns     
    """
    df_arrivals = load_data_arrivals()

    df_arrivals = df_arrivals.dropna(how='all', axis=1)
    df_arrivals = df_arrivals.drop(['Indicator Code'], axis=1)

    return df_arrivals
```
**Breakdown of `drop_year_columns_arrivals()`:**

### **Drop completely empty columns**
```
df_arrivals = df_arrivals.dropna(how='all', axis=1)
```
From the info displayed before, and the reasoning explained in the previous explanation, the 35 empty year columns and the fully empty(null) column was dropped with the above function. The axis set to equal 1 to focus on columns.
<br/>

### **Drop Indicator code column**
```
df_arrivals = df_arrivals.drop(['Indicator Code'], axis=1)
```
By analysing the previous unique values information about columns, it was seen that the "Indicator Code" and "Indicator Name" columns displayed information which both indicated data is about international tourist arrivals. Since the "Indicator Code" column displayed "ST.INT.ARVL" has many abbreviations that could be hard to understand, it was decided to only keep the "Indicator Name Column".
<br/>  
Further exploration of this current dataset is done is continued in a later stage. Instead, the dataset with country metadata is explored and prepared in order to merge it first with the main dataset arrivals.csv to make cleaning easier.
<br/> 
<br/> 

# **Data Exploration of metadata.csv**

### **Loading metadata.csv using a pandas data frame**
```
def load_data_metadata():
    """
    Loads data given filepath using pathlib and processes data 
    as a pandas dataframe

    Args:
        None
    Returns:
        df_metadata: a pandas dataframe on the metadata.csv dataset
    """
    metadata_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'metadata.csv')
    df_metadata = pd.read_csv(metadata_csv, skiprows=0)

    pd.set_option('display.max_rows', df_metadata.shape[0] + 1)
    pd.set_option('display.max_columns', df_metadata.shape[1] + 1)  

    return df_metadata
```
Again, another function was used to load the metadata.csv dataset:
- No rows were skipped as the first row contained apparent column headings
- The pandas display options were set to the number of columns and rows in the dataframe for easier terminal output viewing as explained before.
<br/>
<br/>

### **Exploring and dropping columns in the metadata.csv dataset dataframe**
```
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
    df_metadata = load_data_metadata()
    
    basic_visualise_data(df_metadata)
    
    df_metadata = df_metadata.drop(['SpecialNotes'], axis=1)
    df_metadata = df_metadata.drop(['TableName'], axis=1)
    df_metadata = df_metadata.dropna(how='all', axis=1)

    df_income_regions = df_metadata

    return df_income_regions
```
This function first visualises then drops 3 columns.  
**Breakdown of `drop_columns_metadata()`:**

### **Visualising the shape, head, tail with rows and columns information**
```
basic_visualise_data(df_metadata)
```
This calls the helper function basic_visualise_data() previously used to visualise the dataset. 
- From the terminal output it can be seen that in the head and tail that there is long unneccessary description in the 
**'SpecialNotes'** column so this column can be removed.
- The **'Country Code'** column also seems to show the values, the country codes, which were also in the the `arrivals.csv` dataset. Therefore, this column was selected to be used later as a common column by which to merge the two datasets.
- The **'TableName'** column in `metadata.csv` seems to contain country names which is just the same information that was already contained in the first dataset `arrivals.csv` in **'Country Name'** column. Since the country code will be used to merge common columns, as mentioned above, this column is unneccessary. 
- In the rows and column information, there are 6 columns in total and there is an empty null column is seen at the end of the dataset so this will also be removed.
- After merging, to check if every row value in the **'Country Code'** column matched each dataset, the shape will be checked to see if the number of stays the same before and after merge at 266 rows.

### **Removal of 'SpecialNotes' and 'TableName' columns**
```
# Drop the 'SpecialNotes', 'TableName' columns
df_metadata = df_metadata.drop(['SpecialNotes'], axis=1)
df_metadata = df_metadata.drop(['TableName'], axis=1)
df_metadata = df_metadata.dropna(how='all', axis=1)
```
- This first line in this part of code the unnecessary **'SpecialNotes'** column and the second line of code removed the **'TableName'** column.
- The third line removed all completely null columns in this case just the last column.  

<br/>
<br/>
<br/>

# **Merging arrivals.csv and metadata.csv datasets**

```
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

    print("\nUnique values - 'Country Code' in metadata.csv\n", df_income_regions['Country Code'].unique())
    df_merged = df_arrivals.merge(df_income_regions, how='left', left_on='Country Code', right_on='Country Code')

    df_merged = df_merged.drop(['Country Code'], axis=1)

    return df_merged

```
**Breakdown of merge_arrivals_metadata() function:**
```
print("\nUnique values - 'Country Code' in metadata.csv\n", df_income_regions['Country Code'].unique())
```
The unique values was printed for the column 'Country Code' for the metadata.csv dataset as this column name is common to both arrivals.csv and metadata.csv datasets.
- After inspecting the output, it can be seen the country codes in metadata.csv are identical to 'arrivals.csv' found in a previous section. Therefore, this column will be used as a common column to merge both sets.
```
df_merged = df_arrivals.merge(df_income_regions, how='right', left_on='Country Code', right_on='Country Code')
```
The above function merged the arrivals.csv dataframe with the metadata.csv dataframe.  
- This was done so that the income group and regions are shown with the number of arrivals. These two columns of information will be useful to group the country income types and regions later for analysis. They are also mentioned in the problem statement and questions which refer to these two variables.
- Common columns to both datasets were 'Country Code', so this is what is used to merge via common column values.
<br/>

By default, upon using the `.merge()` in pandas, the two uncommon columns, in this case 'Region' and 'Income Group' will be placed at the right end of the dataframe. In order to move them to a more convenient location the next function is used: 
<br/>
```
df_merged = df_merged.drop(['Country Code'], axis=1)
```
The above line of code removed the 'Country Code' column since it contains information not useful for any further part of the data preparation if the country names are already available which represent similar information (i.e. they both show unique identifiers per country).

## **Reordering columns**
```
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

    # Insert each variable to correct second and third position
    df_merged.insert(1, Region_column.name, Region_column)
    df_merged.insert(2, Income_column.name, Income_column)

    # Print list of column names in new order
    print("\nMerged data - columns reordered check\n", list(df_merged.columns.values)) 

    return df_merged
```
The two remaining uncommon columns in the "metadata.csv" dataset called 'Region' and 'IncomeGroup' are initially moved to the end of the merged dataset when merging, which is disadvantageous since they are information columns. So they would be more useful to be near the start with other columns.  It was chosen to move them in front of 'Country Name' and just before 'Indicator Name' so it is evident that the data in the following columns clearly represent the number of arrivals with the 'Indicator Name' column followed by the year columns.
    
**Breakdown of `reorder_columns()` function:**
### **Pop end columns**
```
Region_column = df_merged.pop('Region')
Income_column = df_merged.pop('IncomeGroup')
```
Each line of code above pops the 'Region' and 'Income' column out of the merged dataframe df_merged, ready to be repositioned.
## **Inserting rows into desired position**
```
df_merged.insert(2, Region_column.name, Region_column)
df_merged.insert(3, Income_column.name, Income_column)
```
- The first line of the code above inserts the 'Region' column in position with index 1, i.e. the second column from the left position..
- The second line of the code above inserts the 'Region' column in position with index 2, i.e. the third column from the left position.
```
print("\nMerged data - columns reordered check\n", list(df_merged.columns.values)) 
```
The above function prints a list of the columns in the new order. From the output, it can be seen the order is now: `'Country Name', 'Country Code', 'Region', 'IncomeGroup', 'Indicator Name'` which shows columns were successfully reordered since `'Region'` and `'IncomeGroup'` were listed just after `'Country Code'` and before '`Indicator Name'`. 
<br/>
<br/>

## **Cleaning the 'Country Name' column function**
```
def country_names_clean(data1, data2):
   
    Checks in the 'Country Names' column for inconsistencies and
    unnecessary rows, particularly country groups by matching with 
    a list of officially recognised names
    Args:
        data1: pandas dataframe of merged datasets
        data2: list containing officially recognised country names
    Returns:
        df_merged: pandas merged dataframe after unneeded rows dropped
    """
    df_merged = data1

    print("\nUnique values - 'Country Name' col\n", df_merged['Country Name'].unique())
  
    country_names_worldbank = data2

    # (This code was adapted from: https://www.interviewqs.com/ddi-code-snippets/rows-cols-python)
    print ("\nRows without World Bank defined countries \n", df_merged.loc[~df_merged['Country Name'].isin(country_names_worldbank)])

    df_merged = df_merged[df_merged['Country Name'].isin(country_names_worldbank)]

    print("\nHead after country group rows drop\n", df_merged.head())
    print("\nShape after country group rows drop\n", df_merged.shape)

    return df_merged
```
**Breakdown of `country_names_clean()` function:**
```
print("\nUnique values - 'Country Name' col\n", df_merged['Country Name'].unique())
```
Firstly, the unique values in the Country name column was printed again to check for the groupings and inconsistencies found earlier.
- After observing the unique values in the 'Country Names' column, some unusual entries can be seen. For example, as found before, 'IDA blend'. Upon researching this, it was found this is a group of countries, which all are already individually listed as separate values in the dataset 'Country Name' column. For example 'Chad' is visible. [2]
- According the World Bank website, which is the same as the datasets being used in this project, the officially recognised countries in the contents which are used in every dataset were found at https://data.worldbank.org/country.
- These countries were used as reference for spelling errors and to ensure only countries are in the 'Country Name' column. Since, the countries in that countries' page are the exact same ones they use on every dataset, it was safe to assume at this point that they could be all included in the current used dataset arrivals.csv and are the main rows of interest. This assumption can be validated later.
<br/>  
```
country_names_worldbank = make_list_country_names()
```

The code above calls a helper function make_list_country_names().  
In this function, a list containing the official country names was simply created by copying and pasting the names from the website list into VSCode, then wrapping each in quotations. Then, by highlighting and using the command Join Lines from the VSCode commands, they were all fit onto lines within the 80-character limit and following PEP8 format. Leading and trailing whitespaces were carefully checked when wrapping in quotations to confirm they weren't present to prevent further inconsistencies.
- The reasoning behind this is to later see which values in 'Country Name' column match. The ones that don't match will most likely be the groupings and will be displayed later to help make a decision on whether to remove them.
- This method also ensures perfect format as no whitespaces are present, and, because these were the officially recognised namings on the World Data Bank website, it can be safely assumed there are no special characters or spelling errors present.

**That helper function `make_list_country_names()` is shown below:**
```
def make_list_country_names():
    """
    Helper function: A variable holding a list is created from 
    officially recognised country names to check for inconsistencies

    Args:
        None
    Returns:
        df_country_names_worldbank: a pandas dataframe on the country_names.csv dataset
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
```
**Now returning to the next line of `country_names_clean()` function:**
```
print ("\nRows without World Bank defined countries \n", df_merged.loc[~df_merged['Country Name'].isin(country_names_worldbank)])
```
(This code was adapted from: https://www.interviewqs.com/ddi-code-snippets/rows-cols-python) [4]  
This function printed rows in `df_merged` dataframe that did not match the `country_names_worldbank` list, in order to make a clearer decision on what to do with them.
- From the displayed rows, there are country groupings such as the `'IDA blend'` and `'IBRD only'` etc. which will not be of any use to the target audience or problem statement. The target audience is looking for specific countries to set up hotels. 
- Some values such as `'Middle East & North Africa'` represent the regions and others like `'Low income'` represent the income group which both do relate to the problem statement and business need. However, since there is a separate column for both of these categories (which is `'Region'` and `'IncomeGroup'` respectively), these rows will also be removed from the 'Country Name' column.
- Another detail that can be observed is the fact that every value here is a group of countries which clearly validates the assumption on the country lists made earlier, that they do contain country groups.
<br/>

### **Drop irrelevant rows with values in 'Country Name' not in the official list of countries**
```
df_merged = df_merged[df_merged['Country Name'].isin(country_names_worldbank)]
```
Therefore, due to the above reasons, any rows containing values in the 'Country Name' column which are not part of the 217 officially recognised countries are dropped (removed) from the dataset with the code above.

```
print("\nHead after country group rows drop\n", df_merged.head())
print("\nShape after country group rows drop\n", df_merged.shape)
```
After the rows were dropped, to check if it worked as expected, the head (the first 5 rows), and the shape were displayed with the above code.
- The head shows in particular the rows with value 'Africa Eastern and Southern' and 'Africa Western and Central' have been successfuly removed.
- The shape shows 217 rows which matched the number of offically recognised countries in the World Data Bank (217) so this step was successful and indicates all unwanted rows were removed.
<br/>
<br/>

## **Checking for empty rows**
```
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
    
    print("\nNumber of rows where all columns are empty\n", df_merged.isna().all(axis=1).sum())
    print("Column information - merged\n", df_merged.info(verbose=True)) 
    print("\nRow with null value in 'IncomeGroup'column:\n", df_merged[df_merged["IncomeGroup"].isnull()])
  
    amount_columns = len(df_merged.axes[1])
    
    print("\nColumns showing initial % of missing values\n", (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))

    count_50_percent = 0.5 * amount_columns

    print("\nNo. of rows with 50% of missing values\n", (df_merged.isnull().sum(axis=1) > count_50_percent).sum())
    print("\nInfo of rows with 50% of missing values\n", df_merged.isnull().sum(axis=1) > count_50_percent)
    print("\nSome Rows with 50% missing values\n", df_merged.loc[[2, 8, 38, 220]])
    
    return df_merged
```
**Breakdown of `empty_rows_check()` function:**
### **Count number of null rows**
```
print("\nNumber of rows where all columns are empty:\n", df_merged.isna().all(axis=1).sum())
```
The above function makes use of `.isna()` to count all rows that were empty as there would be no use for these countries to display any information now for data preparation or in later designing app stages.
- The output indicated `'Number of rows where all columns are empty: 0'` which implied there were no fully empty rows to be analaysed.
```
print("Column information - merged\n", df_merged.info(verbose=True)) 
```
Column details and information were viewed again to see which columns were completely full. 
- From the output `"Column information - merged"`, 3 columns ('Country Name', 'Country Code' and 'Indicator Name'), were completely full, with no null values. This was also previously seen in the seaborn bar chart showing distribution of missing values in columns for the `arrivals.csv` dataset.
-  The 'IncomeGroup' column info shows 216 non-null values meaning 1 value on that column is null. So this will be investigated.
<br/>
```
print("\nRow with null value in 'IncomeGroup'column:\n", df_merged[df_merged["IncomeGroup"].isnull()])
```

The above function prints the row containing the empty value in the `'IncomeGroup'` column.
- The row displayed was `'Venezuala'`. After doing some research to try and do an imputation of the missing value, it was found that Venezuela is officially unclassified in its income level [5]. 
- Therefore, for this columm and value, nothing can be done and is left blank. 
<br/>
<br/>
```
amount_columns = len(df_merged.axes[1])
```

A variable `amount_columns` is defined with the function above which counts of the number of columns.  
This is for use in in the next steps for printing rows with their percentage of empty values. 
```
print("\nColumns showing initial % of missing values\n", (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))
```
The above code was used to print a percentage of missing (nul) values for each row.  
- This was done to an idea of the proportion of the rows that were empty. 
- Some rows, like rows with index 2, had a large percentage of missing values at around 83% for example. These high percentages will be removed. 
- Before that, a lower threshold to the allowed maximum percentage is defined in the next step.
<br/>

## **Rows with over 50% empty values check**
A variable for the lower threshold with 50% of no. of columns defined:
```
count_50_percent = 0.5 * amount_columns
```
By multiplying the variable `amount_columns` by 0.5, the number of columns defined earlier, a lower threshold of 50% of the number of columns is defined in the above line of code.
- Then this will be used to see which rows have more than 50% data missing in the next step. 
<br/>

**Reasoning for 50% figure chosen is as follows:**
- If 50% of columns are allowed to be empty then, 50% of the no. of columns in this dataset = `total no. of columns * 0.5 = 15.5`. 
- The first 5 columns have no null values and are not year columns with numeric (float) data. 
- So taking 5 away from 30: `30 - 5 = 25` year columns. 
- `25 - 15.5 = 10.5` meaning there is approximately at least **10** years of data remaining as the minimum number of non-null year values in the row. 
- 10 years which is 10 non-null values of number of international arrivals in the row is therefore deemed sufficient span of years to compute calculations in later steps as well as in the next coursework.
<br/>
<br/>

## **Visualising rows with greater than 50% missing values**

```
print("\nNo. of rows with 50% of missing values\n", (df_merged.isnull().sum(axis=1) > count_50_percent).sum())
print("\nInfo of rows with >50% of missing values\n", df_merged.isnull().sum(axis=1) > count_50_percent)
```
The first line of code above prints the number of values with over 50% of null values.  
The second line prints true or false statements for each row - true for if the row contains over 50% of missing values and false otherwise.
- The first output `'No. of rows with 50% of missing values: 22'` indicated there were 22 matching rows.
- The next output `'Info of rows with 50% of missing values'` indicated some matching row indices. For example, rows with index 2, 8, 38 and 220 were flagged as `'True'`.  
```
print("\nSome Rows with >50% missing values\n", df_merged.loc[[2, 8, 38, 220]])
```
The code above printed some of the full rows with over 50% missing values. Rows with indices 2, 8, 38, 220 were selected just to visualise some of the flagged rows and decide the steps to take.  
- After doing some research on World Bank Data website, and on the internet, for the missing rows, no data could be found for number of arrivals for these countries. 
- For example for 'Afghanistan', it can be seen there is no data available on World Bank Data: https://data.worldbank.org/indicator/ST.INT.ARVL?locations=AF. 
- If later averages and calculations need to be done, countries with more than 50% of missing data will not be useful or accurate to represent countries over the relatively large time scale of years available. 
- Therefore, due to the above reasons, these country rows were decided to be dropped.
<br/>
<br/>


## **Dropping rows over 50% of missing data**:
**A function was defined to drop rows with over 50% missing data:**
```
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
 
    amount_columns = len(df_merged.axes[1])
    count_50_percent = 0.5 * amount_columns

    df_merged = df_merged.dropna(thresh=count_50_percent, axis=0)

    print("\nShape after >50% null removal\n", df_merged.shape)
    
    print("\nColumns showing % of missing values after 50% null removal\n",
         (100 * (df_merged.isnull().sum(axis=1) / amount_columns)))

    return df_merged
```
**Breakdown of `drop_empty_rows()` function:**
```
amount_columns = len(df_merged.axes[1])
count_50_percent = 0.5 * amount_columns
```
The above lines of code again defines the same 50% of number of columns in dataframe count variable for the same reasons outlined in function `empty_rows_check()` previously.

### **Dropping the over 50% null rows part:**
```
df_merged = df_merged.dropna(thresh=count_50_percent, axis=0)
print("\nShape after >50% null removal\n", df_merged.shape)
print("\nColumns showing % of missing values after 50% null removal\n", 100 * (df_merged.isnull().sum(axis=1) / amount_columns)))
```
The first line of code above drops the rows with over 50% of nulls and the second line prints the shape of the dataframe after.
- The output is `'195'` for number of rows. This is equivalent to no. of rows take away number of flagged over 50% null rows before: `217 - 22 = 195.`
- This shows this step was successful.
- The third line prints the percentage of nulls in each row after the rows were dropped.
- Most of the percentages are very low, and the highest is 45% null values which is within the allowed amount so this further shows the data is ready in terms of null values. 
<br/>
<br/>

## **Final unique values check for the merged dataframe df_merged**
A final check on duplicates and unique values for some columns in the new dataframe are done with the function below:
```
def unique_values_check_remaining_columns(data):
    """
    Checks for duplicates and unique values of the first 4 columns
    
    Args:
        data: the merged pandas dataframe df_merged 
    Returns:
        df_merged: the merged pandas dataframe unaltered 
    """
    
    df_merged = data
  
    print("\nDuplicates in 'Country Name'?\n", df_merged.duplicated(subset=['Country Name']).any().sum())

    print("\nUnique values - 'Region' column\n", df_merged['Region'].unique())
    print("\nUnique values - 'IncomeGroup' column\n", df_merged['IncomeGroup'].unique())
    print("\nUnique values - 'Country Name' column\n", df_merged['Country Name'].unique()) 
 
    return df_merged
```

**Breakdown of `unique_values_check_remaining_columns()`**
### **Duplicates Check:**
```
print("\nDuplicates in 'Country Name'?\n", df_merged.duplicated(subset=['Country Name']).any().sum())
```
Firstly, with the lines of code above, duplicates were checked for the 'Country Name' column where a true or false statement was returned as this is the only column where duplicates should not be present, since each name should be unique for each individual country. 
- The results showed 'false' which confirmed no duplicates in the mentioned column.

### **Second unique values check on merged dataframe"**
**'Region' column check:**
```
print("\nUnique values - 'Region' column\n", df_merged['Region'].unique())
```
A check was done on the unique values in the 'Region' column to check for any inconsistencies. 
- In the terminal output, `'Unique values - 'Region' column'`, there are 7 regions printed: `['Latin America & Caribbean' 'Sub-Saharan Africa' 'Europe & Central Asia' 'East Asia & Pacific' 'South Asia' 'Middle East & North Africa' 'North America']`.
- According to the World Bank Data website [6][7], the 7 regions match completely by observing the spelling and format by eye.
- This implies that this column has no inconsistent values so nothing more needs to be done for this column in terms of inconsistencies.

**'IncomeGroup' column check:**
```
print("\nUnique values - 'IncomeGroup' column\n", df_merged['IncomeGroup'].unique())
```
The above code checked if there are unique values in the IncomeGroup' column again for inconsistencies:
- The output printed 4 income groups: ['High income' 'Lower middle income' 'Upper middle income' 'Low income']. 
- Again, after doing a search on the World Bank Data website [8], these 4 regions matched exactly, so there are no inconsistencies in this column.
- It was considered that `'Lower middle income'` and `'Higher middle income'` essentially could be rewritten as just 'Middle income' but it was decided not to combine these two in order to match the official World Bank Data classifications and have more of a split for more accurate results displayed per region later on when the app is to be made.

**'Country Name' column check:**
```
print("\nUnique values - 'Country Name' column\n", df_merged['Country Name'].unique())
```
A check was done on the 'Country Name' column again, this time to check for any unnecessary words or orderings in names or parts that could possibly be slightly unclear to the user of the data.
- Most of the country names looked clear. However, there were 2 names that were not completely clear. For example, two countries `'Bahamas, The'` and `'Gambia, The'` could be written as `'The Bahamas'` and `'The Gambia'` for clarity since these are each of their actual officially recognised country names. 
- These 2 steps are addressed in the next step and function.
<br/>
<br/>

The `'Indicator Code` column was not checked since it was previously revealed to only contain one unique value that is `'International Tourism, number of arrivals'`.
<br/>
<br/>

## **Renaming country names for clarity**:
```
def clean_names_country_names_column(data):
    """
    Renames certain values in the "Country Name" column with 
    a more useful format

    Args:
        data: the merged pandas dataframe df_merged 
    Returns:
        ds_merged: the merged dataframe after renaming
    """
    
    data = data["Country Name"].replace(["Bahamas, The", "Gambia, The"], ["The Bahamas", "The Gambia"])

    return df_merged
```
The simple function above was used to replace the previously mentioned unclear countries with 'The Bahamas' and 'The Gambia' for clarity.
<br/>
<br/>

## **Basic Statistics for columns
Some basic statistics for columns such as count (count of values in column), mean, std(standard deviation), minimum, maximum, median (50%), lower quartile (25%) and upper quartile(75%) were displayed with the function below to understand the data more, particularly the columns.
```
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

    print("\nBasic stats for df_merged dataframe year columns:\n", df_merged.describe())

    return df_merged
```
**Mean:** 
From the outputs the mean number of arrivals for all countries per year seemed to be increasing each year apart from the year 1997 to 1998 where it dropped from `6.096559e+06` to `5.257463e+06`.

<br/>
<br/>

# **Exporting the prepared merged file:**
Finally, the file was exported using the code below to the `data` folder in this `coursework1` repository.
The file was called **`'Tourism_arrivals_prepared.csv'`**
```
prepared_csv_filepath = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'Tourism_arrivals_prepared.csv')df_merged_final.to_csv(prepared_csv_filepath, index=False)
```
<br/>
<br/>

# **References**  
[1]: https://datavizpyr.com/visualizing-missing-data-with-seaborn-heatmap-and-displot/  
[2]: https://ida.worldbank.org/en/about/borrowing-countries#:~:text=Some%20countries%2C%20such%20as%20Nigeriato%20as%20%E2%80%9Cblend%E2%80%9D%20countries.  
[3]: https://data.worldbank.org/country  
[4]: https://www.interviewqs.com/ddi-code-snippets/rows-cols-python  
[5]: https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2021-2022  
[6]: https://data.worldbank.org/country 
[7]: https://ourworldindata.org/grapher/world-regions-according-to-the-world-bank  
[8]: https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2022-2023#:~:text=The%20World%20Bank%20assigns%20the,the%20previous%20year%20(2021)  
....