import csv

inFile = open('LabDemo.csv', 'r')
outFile = open('CustomerSummary.txt', 'w')
inReader = csv.reader(inFile, delimiter=',')
allPurchases = []
uniqueCustomers = set()
uniqueItems = set()


class Purchase(object):
    def __init__(self, cust=None, sku=None, qty=0.0, price=0.0):
        self.customer = cust
        self.SKU = sku
        self.QTY = qty
        self.price = price


for line in inReader:
    if line[0] != 'custName':
        allPurchases.append(Purchase(cust=line[0], sku=line[1], qty=float(line[2]), price=float(line[3])))
        uniqueCustomers.add(line[0])  # Sets will automatically remove duplicate entries
        uniqueItems.add(line[1])
inFile.close()

for customer in sorted(uniqueCustomers):
    outFile.write("Customer: " + customer + "\n")
    for item in sorted(uniqueItems):
        totalSpent = 0
        totalItems = 0
        for purchase in allPurchases:
            if customer in purchase.customer and item in purchase.SKU:
                totalSpent += (float(purchase.QTY) * float(purchase.price))
                totalItems += int(purchase.QTY)
        if totalItems > 0:
            average = totalSpent / totalItems
            outFile.write('Average Price for ' + item + ': $' + str("%.2f" % average) + '\n')
        else:
            outFile.write('Average Price for ' + item + ': No purchase history \n')
    outFile.write("\n")
outFile.close()
