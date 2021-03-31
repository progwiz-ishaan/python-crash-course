import csv

import matplotlib.pyplot as plt

filename = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high tempretures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high tempretures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Sitka weather daily high tempretures July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Tempreture (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()