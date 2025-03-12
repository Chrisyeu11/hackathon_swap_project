import pandas as pd

# Load Binance trade data
binance_parquet = "cex_trades_binance_ETH_USDT-2024-01.parquet"
print("📥 Loading Binance trade data...")
binance_df = pd.read_parquet(binance_parquet)

# Convert timestamp to datetime for consistency
binance_df["timestamp"] = pd.to_datetime(binance_df["timestamp"], unit="ms")

# ✅ Add an "exchange" column
binance_df["exchange"] = "Binance"

# Save as Swap Data
swap_file = "swap_data_Jan2024.parquet"
binance_df.to_parquet(swap_file, index=False)

print(f"✅ Data collection complete! File saved as {swap_file}")
