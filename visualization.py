import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load price analysis results
output_file = "swap_price_analysis_Jan2024.parquet"
df = pd.read_parquet(output_file)

# Ensure required columns exist
required_columns = ["trade_size_usd", "price_difference_%", "exchange"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Missing required columns in data! Found: {df.columns}")

# Define trade size bins (log scale)
bins = np.logspace(np.log10(df["trade_size_usd"].min()), np.log10(df["trade_size_usd"].max()), num=30)
df["trade_size_bin"] = pd.cut(df["trade_size_usd"], bins)

# Group by bin and exchange, then take the mean of price difference
df_grouped = df.groupby(["trade_size_bin", "exchange"])["price_difference_%"].mean().unstack()

# ✅ Fix: Extract midpoint values from bin categories
bin_midpoints = df["trade_size_bin"].cat.categories.mid
df_grouped.index = bin_midpoints

# Create the plot
plt.figure(figsize=(10, 5))
plt.xscale("log")  # Log scale for trade size
plt.plot(df_grouped, marker="o", linestyle="-")

# Add labels and title
plt.xlabel("Trade Size (USD, Log Scale)")
plt.ylabel("Average Trading Cost (%)")
plt.title("Average Trading Cost for Each Exchange (WETH/USDT)")
plt.legend(title="Exchange")
plt.grid(True, linestyle="--", alpha=0.5)

# Save the figure
plt.savefig("trade_size_vs_avg_cost.png")
plt.show()
