import datetime as  dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Define Time Frame
start = dt.datetime(2021,1,11)  # Games Workshop Group shares which were bought on 11/01/2021
end = dt.datetime.now()         # Current Time

# Load Data from yahoo API
ticker = 'GAW.L'
data = web.DataReader(ticker, 'yahoo', start, end)
print(data.columns)

# Properties of Japanese Candlesticks
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

# Visualization of candlestick chart
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('{} '.format(ticker), color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('darkslateblue')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()
candlestick_ohlc(ax, data.values, width=0.5, colorup='forestgreen', colordown='orangered') # Colours for Japanese candlesticks
plt.xlabel('Date', color='white')
plt.ylabel('Price', color='white')
plt.show()
