from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route("/financial_data", methods=["GET", "POST"])
def display_financial_data():
    ticker_symbol = request.args.get("ticker_symbol")  # Ambil simbol dari form

    if not ticker_symbol:
        return render_template("financial_data.html", ticker=None)

    ticker = yf.Ticker(ticker_symbol)

    # Initialize the financial data dictionary
    financial_data = {
        "Metric": ["Revenue", "Net Income", "EPS", "Dividends", "Free Cash Flow", "LT Debt", "LT Debt/Equity", "Total Shares", "PE Ratio"],
    }

    years = [2023, 2022, 2021, 2020]
    income_statements = ticker.financials
    balance_sheet = ticker.balance_sheet
    cash_flow = ticker.cashflow
    key_stats = ticker.info

    for year in years:
        year_data = []
        try:
            year_str = str(year)
            revenue = income_statements.loc["Total Revenue", year_str].values[0] if "Total Revenue" in income_statements.index else "N/A"
            net_income = income_statements.loc["Net Income", year_str].values[0] if "Net Income" in income_statements.index else "N/A"
            eps = income_statements.loc["Basic EPS", year_str].values[0] if "Basic EPS" in income_statements.index else "N/A"
            dividends = ticker.dividends
            yearly_dividends_f = dividends[dividends.index.year == year].sum() if not dividends.empty else "N/A"
            yearly_dividends = f"{yearly_dividends_f:.2f}"

            free_cash_flow = cash_flow.loc["Free Cash Flow", year_str].values[0] if "Free Cash Flow" in cash_flow.index else "N/A"
            lt_debt = balance_sheet.loc["Long Term Debt", year_str].values[0] if "Long Term Debt" in balance_sheet.index else "N/A"
            total_shares = balance_sheet.loc["Share Issued", year_str].values[0] if "Share Issued" in balance_sheet.index else "N/A"
            #pe_ratio = key_stats.get("trailingPE", "N/A")
        except Exception as e:
            print(f"Error for year {year}: {e}")
            year_data = ["N/A"] * 9

        year_data.extend([revenue, net_income, eps, yearly_dividends, free_cash_flow, lt_debt, "N/A", total_shares, "N/A"])
        financial_data[year] = year_data

    df = pd.DataFrame(financial_data)

    #return render_template("financial_data.html", ticker=ticker_symbol, df=df)
    return render_template("financial_data.html", ticker=ticker_symbol, df=df, key_stats=key_stats)

if __name__ == "__main__":
    app.run(debug=True)
