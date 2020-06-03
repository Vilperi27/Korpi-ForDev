import json
import matplotlib.pyplot as plt

heartRateValues = []
dateTimeValues = []

with open('training-session.txt') as json_file:
    data = json.load(json_file)


    for p in data['exercises']:
        for r in p['samples']['heartRate']:
            heartRateValues.append(r['value'])
            dateTimeValues.append(r['dateTime'])

plt.plot(heartRateValues)
plt.xlabel('Seconds')
plt.ylabel('Heart Rate')
plt.show()