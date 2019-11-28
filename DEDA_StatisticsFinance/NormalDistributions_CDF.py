"""
Description:
 - Plots 3 normal pdfs + histograms
 -

Usage: just roll

Author:
 - Junjie Hu, hujunjie@hu-berlin.de
 - students from SDA Class St Gallen
Last modified date: 20191030
"""

import scipy as sc
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal(mu, sigma, size):
    # Create a function to receive normal distribution parameters
    normal_data = sc.random.normal(loc=mu, scale=sigma, size=size)
    plt.axes()
    # The hist() method not only draw the histogram
    # but also return the info of the drawing
    n, bins, patchs = plt.hist(normal_data, bins=100, density=True)
    # Use bins returned from hist() to draw a wrap line
    y = norm.pdf(bins, mu, sigma)
    # Like LATEX, Use $ and \to mark mathematical symbols
    plt.plot(bins, y, '-', label=f'$\mu={mu}, \sigma={sigma}$')
    plt.draw()
    return plt


mus = (0, 10, 20)
sigmas = (1, 1.5, 3)
sizes = (10000, 10000, 10000)

# Draw 3 plots with different parameters in the same figure
plot = [plot_normal(mu, sigma, size) for mu, sigma, size in zip(mus, sigmas, sizes)][0]
plot.ylabel('Frequency')
plot.title('Normal Distributions Histogram')
plot.legend()
plot.savefig('DEDA_StatisticsFinance/histogram_normal.png', dpi=300)
plot.show()
