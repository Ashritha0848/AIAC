import pandas as pd
import numpy as np
# Read the dataset
df = pd.read_csv('sales_data_before_cleaning.csv')

# Display initial information about the dataset
print("Initial Dataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
# Fill numeric columns with mean
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Fill categorical columns with mode
categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

# Manual Min-Max scaling
def min_max_scale(x):
    return (x - x.min()) / (x.max() - x.min())

# Manual Standard scaling
def standard_scale(x):
    return (x - x.mean()) / x.std()

# Apply normalizations
df['transaction_amount_minmax'] = min_max_scale(df['transaction_amount'])
df['transaction_amount_standard'] = standard_scale(df['transaction_amount'])

# Display results
print("\nAfter Cleaning - Missing Values:")
print(df.isnull().sum())
print("\nSample of normalized transaction amounts:")
print(df[['transaction_amount', 'transaction_amount_minmax', 'transaction_amount_standard']].head())

# Save the cleaned dataset
df.to_csv('sales_data_after_cleaning.csv', index=False)
print("\nCleaned dataset has been saved as 'sales_data_after_cleaning.csv'")

# Read the cleaned dataset to verify
cleaned_df = pd.read_csv('sales_data_after_cleaning.csv')
print("\nVerifying cleaned dataset:")
print(cleaned_df.head())