# plot that data in file sample data.txt

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')

# print(type(data))

# plt.scatter(data['x'], data['y'])
# plt.ylabel('y')
# plt.xlabel('x')
# plt.title('some random title')
#
# plt.show()

#from udemy #

# data.plot(x='x', y='y', kind='scatter')
# plt.show()

# from udemy2

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

output_file('bokeh_plot.html')

f = figure()
f.circle(x=data['x'], y=data['y'])

show(f)
