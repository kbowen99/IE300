import csv

inFile = open("LabDemo.csv", 'r')
outFile = open("out.txt", 'w')

inReader = csv.reader(inFile,delimiter=',')

for line in inReader:
    print(line)
    for col in line:
        outFile.write(col + ' ')
    outFile.write('\n')


outFile.close()
inFile.close()