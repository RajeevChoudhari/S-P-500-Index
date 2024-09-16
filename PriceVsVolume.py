import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sp.csv')
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df['Date'], df['Close'], color='blue', label='Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price (USD)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(df['Date'], df['Volume'], color='red', label='Volume', linestyle='--', alpha = 0.75)
ax2.set_ylabel('Volume (10 billions)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Price and Volume of the S&P 500 Index Over Time')
fig.tight_layout()

# Show the plot
plt.show()
