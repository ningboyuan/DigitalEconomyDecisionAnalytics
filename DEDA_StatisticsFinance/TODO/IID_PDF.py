import numpy as np
import matplotlib.pyplot as plt

dt1 = np.random.randn(100000)
dt2 = np.random.randn(100000)
dt1_hist = plt.hist(dt1, 100)[0]
dt2_hist = plt.hist(dt2, 100)[0]

pdf = dt1_hist + dt2_hist



