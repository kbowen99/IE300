import csv
import numpy as np

# By changing the delimiter, we can just use the CSV library to read our text file
inFile = open('IE300_CASE2_DATA.txt', 'r')
inReader = csv.reader(inFile, delimiter='\t')
claim = []
K = 95

# Retention Values from Table 1
R = [3.0, 3.5, 4.0, 5.0, 7.0]
R = [i * 10**6 for i in R]

# Load all data
for line in inReader:
    claim.append(int(line[1].replace(',', '')))

# Sort ascending
claim.sort()


# Estimator defined in EX3.3
def estimator33(r):
    sum = 0
    for c in claim:
        sum += max(0, c-r) # [x]_+ notation means to only accept values above zero
    return (1.0 / len(claim)) * sum


# Hill Estimator
def estimator_hill(n, k):
    sum = 0
    for ii in range(n-k+1, n):
        sum += np.log(claim[ii]) - np.log(claim[n-k])
    return float(sum) / float(k)


# Estimator defined in EX3.5
def estimator35(r, n, k, hill):
    return (r / (1.0 / hill) - 1.0) * (float(k)/float(n)) * (r / (claim[n-k]))**(-1.0 / hill);


# Do the calculations
for i in R:
    print "For Retention Value: " + str(i) + " Estimator 1 (EX3.3) Predicts a Premium of: " + str(estimator33(i))
    print "For Retention Value: " + str(i) + " Estimator 3 (EX3.5) Predicts a Premium of: " + \
          str(estimator35(i, len(claim), K, estimator_hill(len(claim), K)))


