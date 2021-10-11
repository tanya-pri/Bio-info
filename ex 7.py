# открыватель,
import csv

def atPercentage(strand):
    a, t, g, c = 0, 0, 0, 0
    for i in strand:
        if i == 'a':
            a += 1
        elif i == 't':
            t += 1
        elif i == 'g':
            g += 1
        elif i == 'c':
            c += 1
    at = (a + t) * 100 / (a + t + c + g)
    return at



with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] in ['Drosophila melanogaster', 'Drosophila simulans']:
            print('1:', row[2])
        if 90 <= len(row[1]) <= 100:
            print('2:', row[2])
        if int(row[3]) < 200 and atPercentage(row[1]) > 50:
            print('3:', row[2])
        if row[0] not in ['Drosophila melanogaster'] and (row[2][0] == 'k' or row[2][0] == 'h'):
            print('4:', row[2])
        atLevel = atPercentage(row[1])
        if atLevel > 65:
            print('5:', row[2], 'High')
        elif atLevel > 45:
            print('5:', row[2], 'Medium')
        else:
            print('5:', row[2], 'Low')



