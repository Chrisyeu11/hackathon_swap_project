Hackathon Swap Project  (Christopher Yeu Chrisyeu11@gmail.com)

## Overview
This project collects, processes, and visualizes swap and trade data for a specific market within a given time frame. It integrates data from Binance and Uniswap, processes the swap data, performs price analysis, and generates a visualization to compare trade size with average cost.

## Setup Instructions

### Prerequisites
1. Install Python 3.x.
2. Install dependencies using the following command:
   ```sh
   pip install -r requirements.txt
   ```
3. (Optional) Use a virtual environment to manage dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

## Steps to Run

### 1. Run Data Collection
   Fetch Binance trade data and save it as a Parquet file.
   ```sh
   python fetch_swaps.py
   ```
   - This script reads the Binance trade data and saves it as `swap_data_Jan2024.parquet`.

### 2. Validate Data Collection
   Check if the collected data has the expected format and columns:
   ```sh
   python check_swap.py
   ```
   - This should display the first few rows and confirm that all necessary columns are present.

### 3. Run Price Analysis
   Perform price analysis by comparing swap prices to mid-market prices.
   ```sh
   python price_analysis.py
   ```
   - This generates `swap_price_analysis_Jan2024.parquet`, which includes additional columns such as `price_difference_%`.

### 4. Validate Price Analysis
   Ensure that the price analysis output contains all required fields:
   ```sh
   python check_analysis.py
   ```
   - This verifies that the `exchange` and `price_difference_%` columns are present.

### 5. Generate Visualization
   Create a graph comparing trade size to average trading cost.
   ```sh
   python visualization.py
   ```
   - This creates `trade_size_vs_avg_cost.png`, which visualizes trade size against average cost.

## Challenges and Solutions

### Challenge 1: API Data Unavailability
   - Initially, Uniswap V2 and V3 data were included, but the API endpoint was deprecated.
   - Solution: Switched to using only Binance trade data, which was downloaded manually.

### Challenge 2: Missing Columns
   - The `exchange` and `price_difference_%` columns were missing from the processed data.
   - Solution: Ensured that `exchange` was retained from the original dataset and calculated `price_difference_%` correctly.

### Challenge 3: Visualization Issues
   - The graph was cluttered and unreadable due to large variations in trade sizes.
   - Solution: Applied a logarithmic scale to the x-axis and improved data aggregation by binning trade sizes.

## Expected Outputs
- `swap_data_Jan2024.parquet` → Cleaned swap data from Binance.
- `swap_price_analysis_Jan2024.parquet` → Price analysis with percentage difference.
- `trade_size_vs_avg_cost.png` → Graph showing trade size vs. average cost.





