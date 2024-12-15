import yfinance as yf

# Mendapatkan data untuk BBCA.JK
ticker = 'BBRI.JK'
stock = yf.Ticker(ticker)

# Mengambil laporan keuangan tahunan
financials = stock.financials

# Menampilkan data 'Revenue' untuk tahun terakhir (misalnya 2023)
print("Revenue (2023):", financials.loc['Total Revenue', :])