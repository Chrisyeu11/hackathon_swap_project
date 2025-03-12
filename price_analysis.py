import pandas as pd

# Load swap data
swap_file = "swap_data_Jan2024.parquet"
swap_df = pd.read_parquet(swap_file)

# Convert timestamps to Unix seconds
swap_df["timestamp"] = pd.to_datetime(swap_df["timestamp"])
swap_df["timestamp"] = swap_df["timestamp"].astype(int) // 10**9  # Convert to Unix seconds

# ✅ Ensure we have 'mid_price' and 'volume'
if "mid_price" not in swap_df.columns or "volume" not in swap_df.columns:
    raise ValueError("❌ Required columns ('mid_price' or 'volume') not found in swap data!")

# ✅ Create 'trade_size_usd' (assuming trade size is in 'volume' column)
swap_df["trade_size_usd"] = swap_df["volume"] * swap_df["mid_price"]

# ✅ Calculate price difference (%)
swap_df["price_difference_%"] = (
    (swap_df["mid_price"] - swap_df["mid_price"].mean()) / swap_df["mid_price"].mean()
) * 100

# Save processed data
output_file = "swap_price_analysis_Jan2024.parquet"
swap_df.to_parquet(output_file, index=False)

print(f"✅ Price analysis complete! File saved as {output_file}")

# Display summary
print(swap_df.head())
