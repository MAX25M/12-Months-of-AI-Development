import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# 1. DOWNLOAD: Get data for 4 different sectors
# Tech (AAPL), Energy (XOM), Gold (GLD), and Crypto (BTC-USD)
tickers = ['AAPL', 'XOM', 'GLD', 'BTC-USD']
data = yf.download(tickers, start="2024-01-01", end="2025-12-31")['Adj Close']

# 2. CALCULATE: Daily Returns
# We correlate 'returns' (changes), not 'prices', to be statistically accurate
returns = data.pct_change().dropna()

# 3. COMPUTE: The Correlation Matrix
corr_matrix = returns.corr()

# 4. VISUALIZE: The Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Asset Correlation Heatmap (Foundation for AI Diversification)")
plt.show()

# 5. EXPORT: Save GitHub Repo
corr_matrix.to_csv("asset_correlation_matrix.csv")
