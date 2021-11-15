import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('TKAgg')

direct = r'C:/Users/admin/PycharmProjects/pythonProject4/' + '/DEDA_MachineLearning/'

#1. sigmoid
x = np.linspace(-5, 5, 100) # observation points
z = 1 / (1 + np.exp(-x)) # the function
plt.figure(0)
plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.savefig(direct + 'sigmoid.png', transparent=True)
plt.show()

#2. RELU
def rectified(x): #the function
    return max(0.0, x)
series_in = [x for x in range(-5, 5)]# define a series of inputs; observation poiints
series_out = [rectified(x) for x in series_in]# calculate outputs for our inputs; function values
# line plot of raw inputs to rectified outputs
plt.figure(1)
plt.plot(series_in, series_out)
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.savefig(direct + 'relu.png', transparent=True)
plt.show()

#3. tanh
def tanh(x):# the function
    return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
series_in = np.linspace(-5, 5, 100) # observation points
series_out = [tanh(x) for x in series_in] # function values
plt.figure(2)
plt.plot(series_in, series_out)
plt.xlabel("x")
plt.ylabel("tanh(x)")
plt.savefig(direct + 'tanh.png', transparent=True)
plt.show()

#4 Sigmoid
x1 = np.arange(-5, -0.1, 0.001)# observation points for the left quadrants
x2 = np.arange(0.001, 5, 0.001)# observation points for the right quadrants
y1 = x1 * 0 # 0-line
y2 = np.sign(x2) #sign fct.
fig, ax = plt.subplots()
sns.lineplot(x = x1, y = y1, color = (72/256, 128/256, 181/256)) # 0-line
sns.lineplot(x = x2, y = y2, color = (72/256, 128/256, 181/256)) # 1-line
plt.scatter(x=0, y=0, color = (72/256, 128/256, 181/256), facecolors = 'none') # hollow point (0,0)
plt.scatter(x=0, y=1, color = (72/256, 128/256, 181/256)) # solid point (0,1)
plt.xlabel("x")
plt.ylabel("sgn(x)")
plt.savefig(direct + "Signum Activation Function.png", transparent = True)
plt.show()