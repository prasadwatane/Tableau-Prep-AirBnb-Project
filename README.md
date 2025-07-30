# Tableau-Prep-AirBnb-Project
Used Tableau Prep to show Airbnbs data
1. Introduction

Dataset

The dataset used in this project consists of approximately 75,000 Airbnb listings from across the United States. It includes a wide range of information such as room types, pricing, host information, amenities, cancellation policies, and geographical data like location and zip code.

Problem Statement

The quality of Airbnb’s platform depends on accurate and complete data. Inconsistent data can degrade user experience, mislead pricing strategies, and introduce inefficiencies in business processes. This project aims to address those issues by cleaning and transforming the dataset for reliable analysis.

Objectives

• Identify and resolve data quality issues (missing data, duplicates, formatting inconsistencies)
• Apply data cleaning, profiling and transformation using Tableau Prep
• Integrate Python scripts for advanced processing such as parsing and outlier detection
• Consolidate and reshape the dataset for downstream analysis and visualization
 

2. Data Profiling and Identified Issues

During the initial data profiling using Tableau Prep and exploratory analysis, the following issues were found:

• Missing values in key columns such as ID, host_identity_verified, room_type, and cancellation_policy
• Duplicate records based on IDs and full-row matches
• Inconsistent formats for boolean values (T/F instead of standardized Yes/No)
• Irrelevant columns such as First Review and Description with a high volume of nulls
• Amenities column represented as a stringified dictionary, complicating parsing
• Decimal inconsistencies in numeric columns like bathroom
• Log-transformed price column requiring conversion to real values
 

3. Cleaning and Transformation Steps

The data cleaning process was broken down across four primary data files. All work was performed in Tableau Prep with supplementary Python integration via TabPY.





 

File 1

• Imported ~75,000 records from the raw Airbnb dataset.
• Removed rows with null values in the ID column.
• Eliminated duplicates based on ID.
• Used conditional logic to fill missing values in the room_type column.
• Standardized numeric values in the bathroom column by rounding.


 



 





File 2

• Removed nulls from ID and cancellation_policy columns
• Dropped First Review and Description columns due to irrelevance and excessive nulls
• Performed an inner join with File 1 based on ID, reducing the dataset to ~73,000 records
 





File 3

• Cleaned null values in ID and host_identity_verified
• Converted boolean fields (Instant Bookable, Host Has Profile Pic, Host Identity Verified) from T/F to Yes/No for readability and consistency




 





 



 

 



 

File 4

• Cleaned nulls from fields: ID, Latitude, Longitude, Neighbourhood, Name, and Zip Code
• Removed duplicates across all columns
• Joined with File 3 on ID, and then merged the result with the output from Files 1 & 2
• Imputed Log_Price using the exponential function and calculated Price_in_dollar
• Dropped the Log_Price field and rounded final prices to two decimal places


Pivoting

• Pivoted data by transforming the city column from rows to columns.
• Generated city-wise listing counts for analysis.
• Aggregated data to show listings per city.
• Enabled simplified visualization of geographical trends.


 



 



4. Python Script Implementation

4.1 Parsing Amenities Column

The amenities column was initially stored as a dictionary-like string. To extract key amenities like Wireless Internet, Air Conditioning, and TV, a Python script was used within Tableau Prep using TabPY.

Code Snippet:

import pandas as pd

 

def add_tv_internet_columns(df):

   def parse_amenities(x):

       if isinstance(x, str):

           try:

               # Remove braces, split by comma

               return [item.strip().strip('"') for item in x.strip('{}').split(',')]

           except Exception:

               return []

       return []

 

   def has_tv(amenities):

       return int('TV' in amenities)

 

   def has_internet(amenities):

       return int('Wireless Internet' in amenities or 'Internet' in amenities)

 

   def has_airconditioner(amenities):

       return int('Air conditioning' in amenities)

 

   parsed = df['amenities'].apply(parse_amenities)

   df['TV'] = parsed.apply(has_tv)

   df['Internet'] = parsed.apply(has_internet)

   df['Air Conditioner'] = parsed.apply(has_airconditioner)

   ​return df.drop(columns=['amenities'])

def get_output_schema():

​ return pd.DataFrame({ 

   ​​'id' : prep_int(),

   'TV' : prep_int(),

   'Internet' : prep_int(),

   'Air Conditioner' : prep_int(),

   'log_price': prep_decimal(),

   'property_type': prep_string(),

   'room_type': prep_string(),

   'accommodates': prep_int(),

   'bathrooms': prep_int(),

   'bed_type': prep_string()

})

4.2 Outlier Detection in Pricing

To enhance data accuracy, a second Python script was implemented to identify outliers in price values using the Interquartile Range (IQR) method.

Code Snippet:

#!/usr/bin/env python

# coding: utf-8

# import libraries

import pandas as pd

# Function

def detect_outliers(df):

   return df[df['log_price'] > 10]

5. Results and Insights

• Cleaned and consolidated dataset now contains ~73,000 records.
• Key fields are standardized and imputed.
• Price values are consistent and free of major outliers.
• Boolean and categorical values are unified across all records.
• Amenities data is now structured and analyzable.
• City-wise listing distribution enables geographic trend analysis.
 



 

6. Conclusion

This project illustrates a complete end-to-end data cleaning and transformation workflow for a large, real-world dataset. The integration of Tableau Prep with Python (TabPY) was critical in handling complex fields like amenities and price outliers.

Challenges Faced

• Parsing semi-structured data stored as strings
• Dealing with inconsistent formatting and missing values
• Designing joins to avoid data loss
Lessons Learned

• Data preparation is foundational to trustworthy analysis
• Combining visual tools with scripting expands transformation capabilities
• Thorough data profiling is essential for discovering hidden quality issues
 
