import json

# Explore the stucure of the data.
filename = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))