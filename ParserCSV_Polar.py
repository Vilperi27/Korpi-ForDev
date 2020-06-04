import csv
import matplotlib.pyplot as plt

HRV = []
passed = False
counter = 0

with open('0604test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if(passed and counter > 2):
            e = int(float(row[2]))
            HRV.append(e)
            counter = 0
        counter += 1
        passed = True

plt.plot(HRV)
plt.xlabel('Seconds')
plt.ylabel('Heartrate')
plt.show()