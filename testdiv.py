import yfinance as yf
import pandas as pd

# Define the ticker
ticker_symbol = "NISP.JK"
ticker = yf.Ticker(ticker_symbol)

# Initialize a dictionary to store the data for multiple years
financial_data = {
    "Metric": ["Revenue", "Net Income", "EPS", "Dividends", "Free Cash Flow", "LT Debt", "LT Debt/Equity",
               "Total Shares", "PE Ratio"],
    "2023": [],
    "2022": [],
    "2021": [],
    "2020": [],
}

# Retrieve financial data
financials = ticker.financials  # Income statement
balance_sheet = ticker.balance_sheet  # Balance sheet
cash_flow = ticker.cashflow  # Cash flow statement
key_stats = ticker.info  # Basic info and ratios
dividends = ticker.dividends  # Dividends history

# Convert index to datetime for filtering by year
dividends.index = pd.to_datetime(dividends.index)


# Function to fetch yearly data
def get_yearly_data(year):
    try:
        # Revenue, Net Income for the given year
        revenue = financials.loc['Total Revenue', str(year)]
        revenue_num = revenue.values[0] if not pd.isna(revenue) else "N/A"

        net_income = financials.loc["Net Income", str(year)]
        net_income_num = net_income.values[0] if not pd.isna(net_income) else "N/A"

        # EPS from key stats
        eps = key_stats.get("trailingEps", "N/A")

        # Dividends from the dividend history
        yearly_dividends = dividends[dividends.index.year == year].sum()  # Sum of dividends for the year
        dividends_value = yearly_dividends if yearly_dividends > 0 else "N/A"

        # Free Cash Flow
        free_cash_flow = cash_flow.loc["Free Cash Flow", str(year)].values[0] if "Free Cash Flow" in cash_flow.index else "N/A"

        # Long Term Debt
        lt_debt = balance_sheet.loc["Long Term Debt And Capital Lease Obligation", str(year)].values[0] if "Long Term Debt And Capital Lease Obligation" in balance_sheet.index else "N/A"

        # Stockholders Equity for LT Debt/Equity
        total_stock_holder = balance_sheet.loc["Stockholders Equity", str(year)].values[0] if "Stockholders Equity" in balance_sheet.index else "N/A"
        lt_debt_equity = lt_debt / total_stock_holder if total_stock_holder != 0 else "N/A"

        # Total Shares
        total_shares = balance_sheet.loc["Share Issued", str(year)].values[0] if "Share Issued" in balance_sheet.index else "N/A"

        # PE Ratio
        pe_ratio = key_stats.get("trailingPE", "N/A")

        # Store data for the year
        financial_data[str(year)].append(revenue_num)
        financial_data[str(year)].append(net_income_num)
        financial_data[str(year)].append(eps)
        financial_data[str(year)].append(dividends_value)
        financial_data[str(year)].append(free_cash_flow)
        financial_data[str(year)].append(lt_debt)
        financial_data[str(year)].append(lt_debt_equity)
        financial_data[str(year)].append(total_shares)
        financial_data[str(year)].append(pe_ratio)

    except KeyError as e:
        print(f"Error with year {year}: {e}")
        for key in financial_data.keys():
            if key != "Metric":
                financial_data[key].append("N/A")


# Loop through the years and get the data
for year in range(2020, 2024):
    get_yearly_data(year)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(financial_data)

# Save to CSV or display
#df.to_csv("NISP-financial_summary_2020_2023.csv", index=False)
#print(df)
