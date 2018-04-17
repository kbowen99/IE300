from matplotlib import pyplot as plt
import numpy as np
import math

# Configuration Variables
n = [1, 2, 10, 100]
ncolor = ["red", "green", "blue", "black"]
nlabel = ["n=1", "n=2", "n=10", "std. normal"]

# Std. Normal
mu = 0
variance = 1
sigma = math.sqrt(variance)

# Actual Plotting
Xv = np.linspace(mu - (3.0 * sigma), mu + (3.0 * sigma), 256, endpoint=True)
for i in range(0, len(n)):
    plt.plot(Xv, (n[i]**(n[i]-0.5))/(math.factorial(n[i]-1)) *
             (1 + Xv/np.sqrt(n[i]))**(n[i]-1) * np.exp(-n[i]*(1+Xv/math.sqrt(n[i]))), color=ncolor[i], label='test')

# Formatting
plt.legend(nlabel)
plt.ylim(0, 1)
plt.title('Central limit of fYn(y)')
plt.ylabel('Probability')
plt.xlabel('Density')
plt.savefig("1.4 Plot.png")
plt.show()
