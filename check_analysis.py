import pandas as pd

# Load price analysis results
output_file = "swap_price_analysis_Jan2024.parquet"
analysis_df = pd.read_parquet(output_file)

print("\n📊 Price Analysis Columns:", analysis_df.columns)
print("\n📊 Price Analysis Sample:")
print(analysis_df.head())
