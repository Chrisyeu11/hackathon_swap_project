import pandas as pd

# Load the final swap dataset
swap_file = "swap_data_Jan2024.parquet"
swap_df = pd.read_parquet(swap_file)

print("\n📊 Final Swap Data Columns:", swap_df.columns)
print("\n📊 Final Swap Data Sample:")
print(swap_df.head())
