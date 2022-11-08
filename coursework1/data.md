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

### **exlpore_data_arrivals() function** ###
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

    # Run basic visualiations function defined before
    basic_visualise_data(df_arrivals)

    # Print unique values in first 4 columns
    print("\nUnique values - 'Country Name' col\n", df_arrivals['Country Name'].unique())
    print("\nUnique values - 'Country Code' col\n", df_arrivals['Country Code'].unique())
    print("\nUnique values - 'Indicator Name' col\n", df_arrivals['Indicator Name'].unique())
    print("\nUnique values - 'Indicator Code' \n", df_arrivals['Indicator Code'].unique())
    
    return df_arrivals
```
This function was made to explore the dataset.  
Breaking down function:
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
Breakdown of helper function:
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
-  **'Country Name'** column: It appears to contain names of many countries. However, some groupings of countries seem to be present such as 'IDA blend' which, after research, was found to be a group of countries. These all are already individually listed as separate values in the dataset 'Country Name' column. This is unwanted as the focus is for specific countries - this will be addressed and fixed in a later step.
- **'Country Code'** column: This appears to contain the country codes of each country.
- **'Indicator Name'** and **'Indicator Code'** columns: Previously, in the `basic_visualise_data()` function results for both the head and tail display, it was observed that 'Indicator Name' and 'Indicator Column' had the same values respectively throughout each. The unique value check test was done on both columns to verify the previous assumption that the whole column contained the same indicator throughout.  
The results show one unique value for both with 'International tourism, number of arrivals' and 'ST.INT.ARVL'. This not only proves the assumption, but also confirms there are no whitespaces or inconsistencies in these columns.  
- Both indicator columns are representing the same information so one column can be safely removed in later steps. Particularly, the 'ST.INT.ARVL' information is quite unclear so will be removed.
<br/>
<br/>

## **Drop columns in Tourism_arrivals.csv**
It could be observed from the column details that columns (with index) 4 to 38, as well as 65 and 66 contained all empty values (as represented by the 0 in non-null count column). These were all year columns, except for the last column which was a completely blank column with no heading. This implied that there was no data on number of arrivals for those years at all. After doing some research, it could be concluded there was no data available for these years 1960 to 1994.  
Therefore, it is safe to make the decision to drop all these columns.  
For the year 2021, there was data available on the internet. However, for the purpose of this coursework, where ethical checks would need to be carried out if I wanted to use this external data, it was decided to drop this column as well and just focus on the years provided.  
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
    # Drop empty columns (36 year columns and 1 blank)
    df_arrivals.dropna(how='all', axis=1, inplace=True)
    # Drops 'Indicator Code' column (same info as 'Indicator Name' column)
    df_arrivals.drop(['Indicator Code'], axis=1, inplace=True)

    return df_arrivals
```
Breakdown of `drop_year_columns_arrivals()`:  

### **Drop completely empty columns**
```
df_arrivals.dropna(how='all', axis=1, inplace=True)
```
From the info displayed before, and the reasoning explained in the previous explanation, the 35 empty year columns and the fully empty(null) column was dropped.  
<br/>

### **Drop Indicator code column**
```
df_arrivals.drop(['Indicator Code'], axis=1, inplace=True)
```
By analysing the previous unique values information about columns, it was seen that the "Indicator Code" and "Indicator Name" columns displayed information which both inicated data is about international tourist arrivals. Since the "Indicator Code" column displayed "ST.INT.ARVL" has many abbreviations that could be hard to understand, it was decided to only keep the "Indicator Name Column".
<br/>  
For now no further exploration of this current dataset is done but it is continued in a later stage.
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

### **Exploring and droppping columns in the metadata.csv dataset dataframe**
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
Breakdown of `drop_columns_metadata()`:

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

    # Print unique values in 'Country Code' column
    print("\nUnique values - 'Country Code' in metadata.csv\n", df_income_regions['Country Code'].unique())

    # Merge columns where df['Country Code'] match df_income_regions['Country Code']
    df_merged = df_arrivals.merge(df_income_regions, how='right', left_on='Country Code', right_on='Country Code')
    print("\nInfo\n", df_merged.info(verbose=True)) 

    return df_merged

```


....