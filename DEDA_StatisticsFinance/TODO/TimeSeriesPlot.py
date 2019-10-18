import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sma
import statsmodels.tsa.api as smt
import scipy.stats as scs
import numpy as np


class TimesSeriesAnalysis():
    def __init__(self, data):
        # self.time_axis = data.index
        self.price = data
        self.lreturn = np.log(data / data.shift(1))

    def plot_ts(self, lags=None, figsize=(10, 8), style='bmh'):
        y_axis = self.price
        if not isinstance(y_axis, pd.Series):
            y_axis = pd.Series(y_axis)
        with plt.style.context(style):
            fig = plt.figure(figsize=figsize)
            layout = (3, 2)
            price = plt.subplot2grid(layout, (0, 0), colspan=2)
            log_return = plt.subplot2grid(layout, (1, 0), colspan=2)
            qq_ax = plt.subplot2grid(layout, (2, 0))
            pp_ax = plt.subplot2grid(layout, (2, 1))

            y_axis.plot(ax=price)
            price.set_title('Time Series Analysis Plots')
            smt.graphics.plot_acf(y_axis, lags=lags, ax=log_return, alpha=0.1)
            sma.qqplot(y_axis, line='s', ax=qq_ax)
            qq_ax.set_title('QQ Plot of Log-Return')
            scs.probplot(y_axis, sparams=(y_axis.mean(), y_axis.std()), plot=pp_ax)

            plt.tight_layout()
        return fig



np.random.seed(1)

# plot of discrete white noise
rand_series = np.random.normal(size=1000)
y_axis = trading_data['AAPL']

aapl_analysis = TimesSeriesAnalysis(log_return['AAPL'])
aapl_analysis.plot_ts(lags=30)

