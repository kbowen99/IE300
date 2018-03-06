import csv
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

inFile = open('FlightTime.csv', 'r')
outFile = open('results.txt', 'w')
inReader = csv.reader(inFile, delimiter=',')
allFlights = []
uniqueCarriers = set()
avgCarrierDelay = []
totalTime = 0.0
totalDelays = 0.0


def calctft(d, lori, ldes):
    return .117 * d + .517 * (lori - ldes) + 20


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
        allFlights.append(Flight(fd=line[0], carrier=line[1], flightNum=line[2], origin=line[3], dest=line[4],
                                 depT=line[5], depD=line[6], arrT=line[7], arrD=line[8], ft=line[9]))
        totalTime = totalTime + int(line[9])
        totalDelays = totalDelays + int(line[6]) + int(line[8])
        uniqueCarriers.add(line[1])
inFile.close()
avgDelay = totalDelays / len(allFlights)

print str(len(allFlights)) + " Valid Observances"
print "Target Flight Time: " + str(calctft(1741.16, -87.9, -118.41))
print "Typical Time: " + str(calctft(1741.16, -87.9, -118.41) + avgDelay)

outFile.write(str(len(allFlights)) + " Valid Observances \n")
outFile.write("Target Flight Time: " + str(calctft(1741.16, -87.9, -118.41)) + "\n")
outFile.write("Typical Time: " + str(calctft(1741.16, -87.9, -118.41) + avgDelay) + "\n")


for carrier in uniqueCarriers:
    carrierDelay = 0.0
    numCarrierFlights = 0.0
    for flight in allFlights:
        if carrier in flight.carrier:
            # carrierDelay += flight.departureDelay + flight.arrivalDelay
            #  Not technical delay, but delay based on typical time
            carrierDelay += flight.flightTime - (calctft(1741.16, -87.9, -118.41) + avgDelay)
            numCarrierFlights += 1.0
    avgCarrierDelay.append((carrierDelay / numCarrierFlights))

    print carrier + " averaged a " + str(carrierDelay / numCarrierFlights) + " min delay with a total delay of " \
          + str(carrierDelay) + " min across " + str(numCarrierFlights) + " flights"
    outFile.write(carrier + " averaged a " + str(carrierDelay / numCarrierFlights) + " min delay with a total delay of " \
          + str(carrierDelay) + " min across " + str(numCarrierFlights) + " flights" + "\n")


minLength = avgCarrierDelay[0]
minCarrier = list(uniqueCarriers)[0]
for i in range(0, len(uniqueCarriers)):
    if avgCarrierDelay[i] < minLength:
        minLength = avgCarrierDelay[i]
        minCarrier = list(uniqueCarriers)[i]

print "Fastest Carrier: " + str(minCarrier)
outFile.write("Fastest Carrier: " + str(minCarrier) + "\n")

plt.bar(range(len(uniqueCarriers)), avgCarrierDelay, align='center')
plt.xticks(range(len(uniqueCarriers)), uniqueCarriers)


plt.title('Average Airliner Flight Delay')
plt.ylabel('Avg. Delay (Min.)')
plt.xlabel('Airline Carrier')

plt.show()
