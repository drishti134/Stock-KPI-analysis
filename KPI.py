import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import requests_cache # Just in case

# Create folder for plots
if not os.path.exists('plots'):
    os.makedirs('plots')

companies = {
    'AAPL': '1y', 'MSFT': '6mo', 'TSLA': '3mo', 'NVDA': '9mo', 'GOOGL': '1mo'
}

data_report = {}

for ticker, period in companies.items():
    print(f"Fetching data for {ticker}...")
    
    # We use 'auto_adjust=True' and 'proxy=None' to force a fresh pull
    df = yf.download(ticker, period=period, auto_adjust=True, ignore_tz=True)
    
    if df.empty:
        print(f"FAILED to download {ticker}")
        continue

    # Flatten columns if MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 5. KPI Calculations
    completeness = float(df.notnull().mean().mean() * 100)
    last_date = df.index[-1]
    latency = (datetime.datetime.now() - last_date.replace(tzinfo=None)).days
    
    # Logic checks
    accuracy_check = (df['High'] >= df['Low']).all()
    if isinstance(accuracy_check, pd.Series): accuracy_check = accuracy_check.all()
    
    consistency_check = (df['Volume'] >= 0).all()
    if isinstance(consistency_check, pd.Series): consistency_check = consistency_check.all()
    
    data_report[ticker] = {
        "Period": period,
        "Rows": len(df),
        "Completeness (%)": round(completeness, 2),
        "Latency (days)": latency,
        "Accuracy (%)": 100 if accuracy_check else 0,
        "Consistency (%)": 100 if consistency_check else 0
    }

    # 4. Visualization
    plt.figure(figsize=(10, 4))
    plt.plot(df['Close'], color='tab:blue', linewidth=1.5)
    plt.title(f'{ticker} Stock Price ({period})')
    plt.ylabel('Price (USD)')
    plt.grid(True, alpha=0.3)
    
    # SAVE AS IMAGE
    plot_path = f"plots/{ticker}_plot.png"
    plt.savefig(plot_path)
    print(f"Saved: {plot_path}")
    
    plt.show() # Close this window to move to the next graph
    plt.close()

# Print Final Table
kpi_df = pd.DataFrame(data_report).T
print("\n--- FINAL KPI SUMMARY TABLE ---")
print(kpi_df)
