import csv
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

inFile = open('FlightDelay.csv', 'r')
outFile = open('results.txt', 'w')
inReader = csv.reader(inFile, delimiter=',')
allFlights = []
uniqueCarriers = set()
uniqueOrigins = set()
uniqueDestinations = set()


def pGiven(n_hat=0.0, m=3.0, p=0.0, n=0.0):
    return (n_hat + (m * p)) / (n + m)


class Flight(object):
    def __init__(self, carr=None, orig=None, dest=None, depD=0, arrD=0, isDelayed=False):
        self.carrier = carr
        self.origin = orig
        self.destination = dest
        self.departDelay = depD
        self.arriveDelay = arrD
        self.delayed = isDelayed


for line in inReader:
    # Not Header & Greater than 230 min long (valid info)
    if line[0] != 'Carrier':
        if int(line[3]) + int(line[4]) < 16:
            allFlights.append(Flight(carr=line[0], orig=line[1], dest=line[2], depD=line[3], arrD=line[4], isDelayed=False))
        else:
            allFlights.append(Flight(carr=line[0], orig=line[1], dest=line[2], depD=line[3], arrD=line[4], isDelayed=True))
        uniqueCarriers.add(line[0])
        uniqueOrigins.add(line[1])
        uniqueDestinations.add(line[2])

inFile.close()

print str(len(allFlights)) + " Recorded Data Points."

numDelays = 0.0
for plane in allFlights:
    if plane.delayed:
        numDelays += 1
print str(numDelays) + " Recorded Delays."
print "P(Y)=" + str(numDelays / len(allFlights)) + "; P(N)=" + str(1 - (numDelays / len(allFlights)))


pYes = numDelays / len(allFlights)
pNo= 1 - pYes
pOrigin = 1.0 / len(uniqueOrigins)
pDestination = 1.0 / len(uniqueDestinations)
pCarrier = 1.0 / len(uniqueCarriers)


for airlineCarrier in uniqueCarriers:
    for origin in uniqueOrigins:
        for destination in uniqueDestinations:
            numberWithOrigin = 0.0
            numberWithOriginY = 0.0

            numberWithDestination = 0.0
            numberWithDestinationY = 0.0

            numberWithCarrier = 0.0
            numberWithCarrierY = 0.0

            for flight in allFlights:
                if origin in flight.origin:
                    numberWithOrigin += 1
                    if flight.delayed:
                        numberWithOriginY += 1

                if destination in flight.destination:
                    numberWithDestination += 1
                    if flight.delayed:
                        numberWithDestinationY += 1

                if airlineCarrier in flight.carrier:
                    numberWithCarrier += 1
                    if flight.delayed:
                        numberWithCarrierY += 1

            # Variable Scheme: probability of carrier I (y/n)
            pCarrierIy = pGiven(n_hat=numberWithCarrierY, m=3.0, p=pCarrier, n=numberWithCarrier)
            pCarrierIn = pGiven(n_hat=(numberWithCarrier - numberWithCarrierY), m=3.0, p=pCarrier, n=numberWithCarrier)

            pOriginIy = pGiven(n_hat=numberWithOriginY, m=3.0, p=pOrigin, n=numberWithOrigin)
            pOriginIn = pGiven(n_hat=(numberWithOrigin - numberWithOriginY), m=3.0, p=pOrigin, n=numberWithOrigin)

            pDestIy = pGiven(n_hat=numberWithDestinationY, m=3.0, p=pDestination, n=numberWithDestination)
            pDestIn = pGiven(n_hat=(numberWithDestination - numberWithDestinationY), m=3.0, p=pDestination, n=numberWithDestination)

            # print "Carrier:"
            # print str(pCarrierIy) + "|" + str(pCarrierIn)
            # print "Origin:"
            # print str(pOriginIy) + "|" + str(pOriginIn)
            # print "Destination:"
            # print str(pDestIy) + "|" + str(pDestIn)

            probDelay = pYes * pCarrierIy * pOriginIy * pDestIy
            probNoDelay = pNo * pCarrierIn * pOriginIn * pDestIn

            if probDelay >= probNoDelay:
                print origin + "-" + destination + " on " + airlineCarrier + " Will be delayed."
            else:
                print origin + "-" + destination + " on " + airlineCarrier + " Will Not be delayed."

            print "Probability of a delay: " + str(probDelay) + " Probability No Delay: " + str(probNoDelay)
