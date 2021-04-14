import json

# Explore the stucure of the data.
filename = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

print(mags[:10])
print(lons[:5])
print(lats[:5])