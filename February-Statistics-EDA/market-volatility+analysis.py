import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your Finance Dataset (e.g., S&P 500 or Bitcoin data)
df = pd.read_csv("stock_market_data.csv")

# 2. Calculate Daily Returns (%)
# Formula: ((Price_Today - Price_Yesterday) / Price_Yesterday) * 100
df['Returns'] = df['Close'].pct_change() * 100

# 3. Statistical Summary
mean_return = df['Returns'].mean()
std_dev = df['Returns'].std()

# 4. The "Distinction" Calculation: Volatility
# In Finance, Volatility = Standard Deviation of Returns
print(f"Daily Average Return: {mean_return:.4f}%")
print(f"Market Volatility (Std Dev): {std_dev:.4f}%")

# 5. Visualizing the Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Returns'].dropna(), kde=True, color='blue')
plt.axvline(mean_return, color='red', linestyle='--', label='Mean')
plt.title("Distribution of Financial Returns (Statistical Analysis)")
plt.legend()
plt.show()
