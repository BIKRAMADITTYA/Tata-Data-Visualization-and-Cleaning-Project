import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv(r"C:\Users\admin\Desktop\Tata project\Online Retail Data Set.csv", )

print(df.head())
print(df.columns)
print(df.info())

#Check Null Values in each column
print(df.isnull().sum())


# Check Duplicate Rows
Duplicate=(df.duplicated().sum())
print("Number of duplicate rows :", Duplicate)

print("Total Row before cleaning",len(df))


#  Check: Quantity  < 1
invalid_quantity_rows = (df['Quantity'] < 1).sum()
print("invalid Rows <1 :",invalid_quantity_rows)


#check for valid unit prices (unit price should be >= 0)
invalid_Unitprice_rows=(df['UnitPrice'] < 0).sum()
print("Invaid Unitprice Rows <0 :", invalid_Unitprice_rows)

          
          ## 🔧 Data Cleaning: Handling Missing and Invalid Values

# Drop rows where CustomerID is missing
df = df[df['CustomerID'].notnull()]

# Fill missing descriptions with a placeholder
df['Description'] = df['Description'].fillna('Unknown')


# Remove rows with quantity less than 1
df = df[df['Quantity'] >= 1]

# Remove rows with unit price less than 0
df = df[df['UnitPrice'] >= 0]

# Remove duplicate rows
df=df.drop_duplicates()


#  Recheck after cleaning
print("Missing Values After Cleaning",df.isnull().sum())
print("Total Row After cleaning",len(df))

print("Invalid Rows <1 after cleaning:", (df['Quantity'] < 1).sum())
print("Invalid UnitPrice <0 after cleaning:", (df['UnitPrice'] < 0).sum())





# Save the cleaned data to a new CSV file

#df.to_csv(r"C:\Users\admin\Desktop\Tata project\Online_Retail_Cleaned.csv", index=False)
#print("✅ CSV saved successfully.")
