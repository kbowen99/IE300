import csv
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np

# By changing the delimiter, we can just use the CSV library to read our text file
inFile = open('IE300_CASE2_DATA.txt', 'r')
inReader = csv.reader(inFile, delimiter='\t')
claim = []

# Since data is already sorted (descending), we can just grab the first 270 observations
for line in inReader:
    if len(claim) < 270:
        claim.append(int(line[1].replace(',', '')))

# Sort ascending
claim.sort()

# Exponential Quartiles
# Map our data
Xv = np.linspace(0, 270, num=270, endpoint=False)
Yv = -np.log((270 - (Xv - 0.5)) / 270)
# Plot our data
plt.plot(Yv, claim)
plt.plot(np.unique(Yv), np.poly1d(np.polyfit(Yv, claim, 1))(np.unique(Yv)), "-.")
# Formatting
plt.title('EX2.3 Exponential QQ Plot')
plt.ylabel('Log Transformed Claim Data')
plt.xlabel('Exponential Quartile')
# Setting bbox_inches forces the labels into the graph region (only an issue since our labels are large)
plt.savefig("2.3 Exponential Plot.png", bbox_inches='tight')
plt.show()

# Normal Quartiles
# Map the data
Xv = np.linspace(1, 270, num=270, endpoint=False)
Yv = norm.ppf((Xv - 0.5) / 270)
# Plot it
plt.plot(Yv, claim)
plt.plot(np.unique(Yv), np.poly1d(np.polyfit(Yv, claim, 1))(np.unique(Yv)), "-.")
# Formatting
plt.title('EX2.3 Normal QQ Plot')
plt.ylabel('Log Transformed Claim Data')
plt.xlabel('Normal Quartile')
plt.savefig("2.3 Normal Plot.png", bbox_inches='tight')
plt.show()
