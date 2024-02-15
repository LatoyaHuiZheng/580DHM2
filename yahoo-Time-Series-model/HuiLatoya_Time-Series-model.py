import pandas as pd

# read data
df = pd.read_csv("/Users/latoyazheng/Desktop/580D HM2/yahoo-finance-scraper/HuiLatoya_stock_data.csv")

# Convert string time to datetime object
from dateutil import parser

def parse_date_range(date_range_str):
    # Split date range string by "-"
    dates = date_range_str.split(' - ')
    # Parse start and end dates
    start_date = parser.parse(dates[0])
    end_date = parser.parse(dates[1])
    return start_date, end_date

# Apply parsing functions in DataFrame
df['start_date'], df['end_date'] = zip(*df['earnings_date'].apply(parse_date_range))

# Set date as index
df.set_index('earnings_date', inplace=True)

# View the first few rows of data
print(df.head())

# Statistical description
print(df.describe())

# Visualize data
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
df['regularMarketPrice'].plot(label='Regular Market Price')
plt.title('Regular Market Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
