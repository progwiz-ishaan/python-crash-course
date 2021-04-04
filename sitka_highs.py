import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high tempretures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y/m%/%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high tempretures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Sitka weather daily high tempretures July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Tempreture (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()