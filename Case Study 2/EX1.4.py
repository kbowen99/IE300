import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
import scipy.misc as spm
import math
from matplotlib import style
import csv

# Configuration Variables
n = [1,2,10,100]
ncolor = ["red", "green", "blue", "black"]
# Std. Normal
mu = 0
variance = 1
sigma = math.sqrt(variance)

# Actual Plotting
X = np.linspace(mu - (3*sigma), mu + (3*sigma), 256, endpoint=True)

for i in range(0, len(n)):
    yn = n[i]**(n[i]-1 /2)/spm.factorial(n[i]-1)*(1+X/n[i]**.5)**(n[i]-1)*np.exp(-n[i]*(1+X/n[i]**.5))
    plt.plot(X, yn, color=ncolor[i])
    print n[i]

plt.ylim(0,9)
plt.title('Central limit of fYn(y)')
plt.ylabel('Probability')
plt.xlabel('Density')
plt.savefig("1.4 Plot.png")
plt.show()