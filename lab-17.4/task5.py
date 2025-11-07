import pandas as pd
import numpy as np

def preprocess_financial_data(file_path):
    try:
        # Read the dataset
        df = pd.read_csv(file_path)

        # ✅ Correct numeric column names
        numeric_columns = ['stock_price', 'volume']

        # ✅ Handle missing values
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

        # ✅ Create moving averages
        df['7_day_ma'] = df['stock_price'].rolling(window=7).mean()
        df['30_day_ma'] = df['stock_price'].rolling(window=30).mean()

        # Fill missing MA values
        df[['7_day_ma', '30_day_ma']] = df[['7_day_ma', '30_day_ma']].fillna(method='ffill')

        # ✅ Standardization: manual z-score
        for col in numeric_columns:
            mean = df[col].mean()
            std = df[col].std()
            df[f"{col}_normalized"] = (df[col] - mean) / std

        # ✅ Encode categorical columns
        categorical_columns = ['sector', 'company_name']
        for col in categorical_columns:
            if col in df.columns:
                df[f"{col}_encoded"] = df[col].astype('category').cat.codes

        # 🧹 Remove duplicates if any
        df = df.drop_duplicates()

        return df

    except FileNotFoundError:
        print("Error: File not found")
        return None
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


# ✅ Execute the preprocessing
if __name__ == "__main__":
    file_path = "financial_dataset_raw.csv"
    processed_df = preprocess_financial_data(file_path)

    if processed_df is not None:
        print("Preprocessing completed successfully ✅")
        print(processed_df.head())
        processed_df.to_csv("processed_financial_data.csv", index=False)
