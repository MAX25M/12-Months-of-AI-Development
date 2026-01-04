import pandas as pd
import numpy as np

# 1. Create a "Dirty" Dataset
raw_data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eve', 'Frank'],
    'Score': [95, 88, np.nan, 95, 700, 45], # nan is missing, 700 is an error/outlier
    'Date': ['2026-01-01', '2026/01/02', 'Jan 3, 2026', '2026-01-01', '2026-01-05', '2026-01-06']
}

df = pd.DataFrame(raw_data)

# --- THE CLEANING PROCESS ---

# A. Remove Duplicates (Alice is in twice)
df = df.drop_duplicates()

# B. Handle Missing Values (Charlie's score)
# We fill it with the average (mean) score
df['Score'] = df['Score'].fillna(df['Score'].mean())

# C. Fix Outliers (Eve's score of 700 is impossible)
# If score > 100, we cap it at 100
df.loc[df['Score'] > 100, 'Score'] = 100

# D. Standardize Dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("Cleaned Data Portfolio Asset:")
print(df)

# Save the cleaned version
df.to_csv("cleaned_student_data.csv", index=False)
