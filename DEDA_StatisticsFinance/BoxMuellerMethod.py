import numpy as np
import matplotlib.pyplot as plt

direct = r'C:/Users/admin/PycharmProjects/pythonProject4/' + '/DEDA_StatisticsFinance/'

np.random.seed(1234)
n = 500
msize = 2

a = np.random.exponential(scale=1, size=n)
phi = np.random.uniform(low=0, high=2 * np.pi, size=n)

x = a * np.cos(phi)
y = a * np.sin(phi)

plt.figure(figsize=(7,7))
plt.plot(x,y,'.r',markersize=msize)
plt.savefig(direct + 'two-dim-normal.png',dpi=300,transparent=True)
plt.show()

A = [[3,1],[1,1]]
A_eig = np.linalg.eig(A)
E_val = A_eig[0]
Gamma = A_eig[1]
Lambda = np.diag(E_val)
np.sqrt(Lambda)
Lambda12 = np.sqrt(Lambda)
A12 = np.dot(np.dot(Gamma, Lambda12), np.transpose(Gamma))

c = [x,y]
tfxy = np.dot(A12, c)
plt.plot(tfxy[0], tfxy[1], '.r', markersize=msize)
plt.savefig(direct + 'two-dim-normal-with-cov.png',dpi=300, transparent=True)
plt.show()