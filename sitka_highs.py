import csv

filename = 'C:/Users/ishaa/Documents/Python-Scripts/python-crash-course/data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)