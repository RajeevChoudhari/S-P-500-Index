import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('sp.csv')
df = pd.DataFrame(data)

# Calculate daily returns
df['Daily Return'] = df['Close'].pct_change() * 100
df = df.dropna()

# Filter out rows with zero volume
df = df[df['Volume'] > 0]

# Create a categorical column for year ranges or specific periods
df['Year'] = pd.to_datetime(df['Date']).dt.year
bins = [1928, 1950, 1975, 2000, 2021]
labels = ['1928-1950', '1950-1975', '1975-2000', '2000-2021']
df['Year Range'] = pd.cut(df['Year'], bins=bins, labels=labels, right=False)

# Set up the plot
sns.set(style='whitegrid')
plt.figure(figsize=(10, 5))
scatter = sns.scatterplot(x='Volume', y='Daily Return', data=df, edgecolor=None, hue='Year Range', palette='viridis', legend='full')
plt.title('Volume vs. Daily Price Change of the S&P 500 Index 1928-2021')
plt.xlabel('Volume')
plt.ylabel('% Change')

# Add a legend with a title
plt.legend(title='Year Range', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
