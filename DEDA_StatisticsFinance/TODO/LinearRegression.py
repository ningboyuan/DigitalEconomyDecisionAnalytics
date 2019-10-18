
import pandas as pd
import datetime
import os
import numpy as np



# Read Apple daily price and calculate the monthly return
apple_stock = pd.read_csv(os.getcwd() + '/DEDA_Class_2017_Statistics&Finance/AAPL.csv', index_col='date', parse_dates=True)
apple_stock_return = apple_stock['return'].to_frame()
apple_stock_return['return'] += 1

apple_stock_return['month'] = [(date.year, date.month) for date in apple_stock_return.index]

apple_stock_return.set_index(keys='month', drop=True, inplace=True)

# Aggregate the return using groupby()
# Multiply all daily return to yield monthly return
apple_stock_return_grouped = apple_stock_return.groupby(by=apple_stock_return.index, axis=0).prod()
apple_stock_monthly_return = apple_stock_return_grouped - 1

ff_factors = pd.read_csv(os.getcwd() + '/DEDA_Class_2017_Statistics&Finance/FF_3Factor_Benchmark.txt', sep='\s+')
# Adjust
ff_factors.set_index([])


