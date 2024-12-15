import yfinance as yf
import pandas as pd

# Define the ticker
ticker_symbol = "NISP.JK"  # Contoh untuk ticker BBCA
ticker = yf.Ticker(ticker_symbol)

# Initialize years list
years = [2023, 2022, 2021, 2020]

# Initialize a dictionary to store dividends data for each year
dividends_data = {}

# Retrieve dividend data
dividends = ticker.dividends

# Convert index to datetime for filtering by year
dividends.index = pd.to_datetime(dividends.index)

# Loop through the years and fetch the dividends
for year in years:
    # Filter for the selected year
    yearly_dividends = dividends[dividends.index.year == year].sum()

    # Handle case where no dividends exist
    dividends_value = yearly_dividends if yearly_dividends > 0 else "N/A"

    # Store the result
    dividends_data[year] = dividends_value

# Print the results for each year
for year, value in dividends_data.items():
    print(f"Dividends for {year}: {value}")
