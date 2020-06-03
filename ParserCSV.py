import csv
import matplotlib.pyplot as plt

MMScore = []
passed = False
counter = 0

with open('MyData.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if(passed and counter == 9):
            e = int(float(row[3]))
            MMScore.append(e)
            counter = 0
        counter += 1
        passed = True

plt.plot(MMScore)
plt.xlabel('Minute')
plt.ylabel('MM score')
plt.show()