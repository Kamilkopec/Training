# create a script that uses the attached file
#  as data source and prints out the top 5 most densely populated
# countries
import pandas as pd

data = pd.read_csv('countries-by-area.txt')

data['density'] = data['population_2013'] / data['area_sqkm']
data = data.sort_values(by='density', ascending=False)

print(data[:5])
