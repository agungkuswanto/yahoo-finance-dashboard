import yfinance as yf
import pandas as pd

# Define the ticker
ticker_symbol = "NISP.JK"
ticker = yf.Ticker(ticker_symbol)

# Initialize the financial data dictionary
financial_data = {
    "Metric": ["Revenue", "Net Income", "EPS", "Dividends", "Free Cash Flow", "LT Debt", "LT Debt/Equity",
               "Total Shares", "PE Ratio"],
}

# Retrieve quarterly financial data
quarterly_financials = ticker.quarterly_financials  # Quarterly income statement
quarterly_balance_sheet = ticker.quarterly_balance_sheet  # Quarterly balance sheet
quarterly_cashflow = ticker.quarterly_cashflow  # Quarterly cash flow statement
key_stats = ticker.info  # Basic info and ratios

# Initialize dictionaries to store the data for each quarter
dividends_data = {}
eps_data = {}

# Retrieve dividend data
dividends = ticker.dividends
dividends.index = pd.to_datetime(dividends.index)

print ("KOLOM START")
print (quarterly_financials)
print ("KOLOM END")
# Loop through available quarterly financials (using the datetime index)
for date in quarterly_financials.columns:
    try:
        quarter_data = []
        year_str = str(date.year)  # Extract the year from the date
        print(f"Processing data for {year_str} ...")

        # Filter and process only 2024 data
        if year_str == '2024':
            #print(f"Processing data for {date.strftime('%Y-%m-%d')}...")

            # Revenue and Net Income
            revenue = quarterly_financials.loc["Total Revenue", date]
            net_income = quarterly_financials.loc["Net Income", date]

            # EPS and Dividends
            eps = quarterly_financials.loc["Basic EPS", date]# if "Basic EPS" in quarterly_financials.index else "N/A"
            eps_data[date] = eps

            # Calculate dividends for the quarter
            # Avoid timezone issues by extracting year and quarter directly from datetime
            quarter_start = pd.Timestamp(year=date.year, month=date.month, day=1)
            quarterly_dividends = dividends[dividends.index.to_period('Q') == quarter_start.to_period('Q')].sum()
            dividends_value = quarterly_dividends if quarterly_dividends > 0 else "N/A"
            dividends_data[date] = dividends_value

            # Free Cash Flow
            free_cash_flow = quarterly_cashflow.loc["Free Cash Flow", date]

            # LT Debt and LT Debt/Equity
            lt_debt = quarterly_balance_sheet.loc["Long Term Debt And Capital Lease Obligation", date]
            total_stock_holder = quarterly_balance_sheet.loc["Stockholders Equity", date]
            lt_debt_equity = lt_debt / total_stock_holder if total_stock_holder != 0 else "N/A"

            # Total Shares
            total_shares = quarterly_balance_sheet.loc["Share Issued", date]

            # PE Ratio
            pe_ratio = key_stats.get("trailingPE", "N/A")

            # Append all metrics for the quarter
            quarter_data.extend([revenue, net_income, eps_data[date], dividends_data[date], free_cash_flow, lt_debt, lt_debt_equity, total_shares, pe_ratio])

            # Add the quarter data to the financial_data dictionary
            financial_data[date] = quarter_data

    except KeyError as e:
        print(f"Error with {date}: {e}")
        # Fill missing data with 'N/A'
        quarter_data = ["N/A"] * 9

# Convert the dictionary to a DataFrame
df = pd.DataFrame(financial_data)

# Save to CSV or display
#df.to_csv("BBCA-2024-quarterly-financial_summary.csv", index=False)
print(df)
