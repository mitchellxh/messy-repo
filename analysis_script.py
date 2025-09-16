import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load sales data
data = pd.read_csv('data/sales_data.csv')

# Basic analysis
print("Sales Data Analysis")
print("===================")
print(f"Total records: {len(data)}")
print(f"Average sales: ${data['Sales'].mean():.2f}")

# Plot sales by region
plt.figure(figsize=(10, 6))
data.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title('Sales by Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()