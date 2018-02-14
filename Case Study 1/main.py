import csv
from  matplotlib import pyplot as plt

inFile = open('FlightTime.csv', 'r')
outFile = open('results.txt', 'w')
inReader = csv.reader(inFile, delimiter=',')
allFlights = []
uniqueCarriers = set()
totalTime = 0
totalDelays = 0

def calcTFT(d, lori, ldes ):
    return .117 * d + .517 * (lori - ldes) + 20;


class Flight(object):
    def __init__(self, fd=None, carrier=None, flightNum=0, origin=None, dest=None, depT=0, depD=0, arrT=0, arrD=0, ft=0):
        self.flightDate = fd
        self.carrier = carrier
        self.number = flightNum
        self.origin = origin
        self.destination = dest
        self.departureTime = depT
        self.departureDelay = int(depD)
        self.arrivalTime = arrT
        self.arrivalDelay = int(arrD)
        self.flightTime = int(ft)


for line in inReader:
    # Not Header & Greater than 230 min long (valid info)
    if line[0] != 'Flight Time' and line[5] != "" and line[7] != "" and line[9] > 230:
        allFlights.append(Flight(fd=line[0], carrier=line[1], flightNum=line[2], origin=line[3], dest=line[4], depT=line[5], depD=line[6], arrT=line[7], arrD=line[8], ft=line[9]))
        totalTime = totalTime + int(line[9])
        totalDelays = totalDelays + int(line[6]) + int(line[8])

        uniqueCarriers.add(line[1])
inFile.close()

totalDelays = 0
for f in allFlights:
    totalDelays = totalDelays + f.arrivalDelay + f.departureDelay
avgDelay = totalDelays / len(allFlights)

print str(len(allFlights)) + " Valid Observances"
print "Target Flight Time: " + str(calcTFT(1741.16, -87.9, -118.41))
print "Typical Time: " + str(calcTFT(1741.16, -87.9, -118.41) + avgDelay)