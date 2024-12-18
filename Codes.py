#For cleaning and other EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'FoodImports.csv'  # Replace with your file path
data = pd.read_csv(file_path, encoding='Latin1')

# Step 1: Display Basic Information about the Dataset
print("Dataset Information:")
print(data.info())

print("\nFirst 5 Rows of the Dataset:")
print(data.head())

print("\nStatistical Summary of Numeric Columns:")
print(data.describe())

# Step 2: Check for Missing Values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())
data = data.fillna(0)

#Verifying if Null Values are Filled
print("\nMissing Values After Filling:")
print(data.isnull().sum())

print("\nUnique Categories in 'Commodity' Column:")
print(data['Commodity'].nunique(), "unique commodities")

