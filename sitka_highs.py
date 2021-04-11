import csv

import matplotlib.pyplot as plt 

filename = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures form this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high temptures.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Format plots
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()