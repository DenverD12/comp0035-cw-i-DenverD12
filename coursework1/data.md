aa# **Data preparation and understanding**

## **Import required libraries**
```
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from pathlib import Path
```

## **Data Exploration of Tourism_arrivals.csv**

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
- Last 2 written lines before the return statement were to set pandas display options to the number of columns and rows in the dataframe.
<br/>

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
- The first 4 columns were also non-null which shows there was no missing values in them.
- The remaining columns seemed to be different years between 1960 and 2021 as well as an empty columns at the end represented by "Unnamed: 66" column name. They all had the datatype "flot 66" which indicated these contained float numbers. These values are the correct datatype to be used in calculations later on.
- There were many columns with 0 non-nulls which indicate completely empty year columns. This could mean the year data for every country on number of international arrivals was missing. A decision will later be made on what to do with these.
<br/>
<br/>

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
-  "Country Name" column: It appears to contain names of many countries. However, some groupings of countries seem to be present such as 'IDA blend' which, after research, was found to be a group of countries. These all are already individually listed as separate values in the dataset 'Country Name' column. This is unwanted as the focus is for specific countries - this will be addressed and fixed in a later step.
- 'Indicator Name' and 'Indicator Code' columns: From both the head and tail results before, it was observed that 'Indicator Name' and 'Indicator Column' had the same values respectively throughout each. The unique value check test was done on both columns to verify the previous assumption that the whole column contained the same indicator throughout.  
The results show one unique value for both with 'International tourism, number of arrivals' and 'ST.INT.ARVL'. This not only proves the assumption, but also confirms there are no whitespaces or inconsistencies in these columns.  
- Both indicator columns are representing the same information so one column can be safely removed in later steps. Particularly, the 'ST.INT.ARVL' information is quite unclear so will be removed.

<br/>
<br/>

## **Drop columns in Tourism_arrivals.csv**
It could be observed from the column details that columns (with index) 4 to 38, as well as 65 and 66 contained all empty values (as represented by the 0 in non-null count column). These were all year columns, except for the last column which was a completely blank column with no heading. This implied that there was no data on number of arrivals for those years at all. After doing some research, it could be concluded there was no data available for these years 1960 to 1994.  
Therefore, it is safe to make the decision to drop all these columns.  
For the year 2021, there was data available on the internet. However, for the purpose of this coursework, where ethical checks would need to be carried out if I wanted to use this external data, it was decided to drop this column as well and just focus on the years provided.  
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
By analysing the previous info about columns, it can be seen that the "Indicator Code" and "Indicator Name" columns displayed the same information - both are inicating data is about arrivals. Since the "Indicator Code" column displayed "ST.INT.ARVL" which has many abbreviations, which can be hard to understand, it was decided to only keep the "Indicator Name Column".  
<br/>

## **Data Exploration of metadata.csv**

### **Loading metadata.csv using a pandas data frame**
```
def load_data_metadata():

    metadata_csv = Path(__file__).parent.parent.joinpath('coursework1', 'data', 'metadata.csv')
    df_income_regions = pd.read_csv(metadata_csv, skiprows=0)

    pd.set_option('display.max_rows', df_income_regions.shape[0] + 1)
    pd.set_option('display.max_columns', df_income_regions.shape[1] + 1)  

    return df_income_regions
```
Again, another function was used to load the metadata.csv dataset:
- No rows were skipped as the first row contained apparent column headings
- Lastly, the pandas display options were set to the number of columns and rows in the dataframe.  

### **Loading metadata.csv using a pandas data frame**
....