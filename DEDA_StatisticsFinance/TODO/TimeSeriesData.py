import pandas as pd
import pandas_datareader.data as data
import numpy as np

# Getting Apple, Microsoft, Amazon data from Yahoo Finance

# Using lambda to create a function
firm_data = lambda x: data.DataReader(name=x, data_source='yahoo', start='2010-01-01', end='2017-01-01')['Adj Close']
firms = ['AAPL', 'MSFT', 'AMZN']
# Creating a DataFrame through dictionary
trading_data = pd.DataFrame({symbol: firm_data(symbol) for symbol in firms})
# Log return calculation
log_return = np.log(trading_data / trading_data.shift(1))
log_return.dropna(inplace=True)
