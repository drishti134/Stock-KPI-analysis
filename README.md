NASDAQ Data Quality Analysis
Author: Drishti Roy

Overview
This repository contains a Python-based pipeline designed to collect financial data and evaluate its quality through specific Key Performance Indicators (KPIs). The goal was to determine if the dataset is reliable enough for training AI models.

1. Data Source
I extracted historical stock data for five NASDAQ companies using the yfinance API. To test the pipeline's versatility, I pulled data over varying timeframes:
•	AAPL: 1 Year
•	MSFT: 6 Months
•	TSLA: 3 Months
•	NVDA: 9 Months
•	GOOGL: 1 Month

2. KPI Results
Each dataset was passed through a validation script to measure four quality metrics. The results confirmed that the data is highly consistent.
Ticker	Period	Data Rows	Completeness	Latency	Accuracy	Consistency
AAPL	1y	252	100%	0 days	100%	100%
MSFT	6mo	125	100%	0 days	100%	100%
TSLA	3mo	63	100%	0 days	100%	100%
NVDA	9mo	190	100%	0 days	100%	100%
GOOGL	1mo	21	100%	0 days	100%	100%

Metric Breakdown:
•	Completeness: Verified that no trading days were missing or null.
•	Latency: Confirmed the data is up-to-date with 0 days of lag from the last market close.
•	Accuracy: Validated that daily high prices were never lower than daily low prices.
•	Consistency: Checked that trading volumes remained non-negative.

3. Visualizations
Basic price trend visualizations for each stock were generated to visually inspect the data for anomalies. These can be found in the /plots directory of this repository.

4. Conclusion	
The analysis shows that the data pulled from the Yahoo Finance API is structurally sound. Because it passed all logic and completeness checks with a 100% success rate, this dataset is considered "clean" and ready for use in machine learning or descriptive statistical analysis.

