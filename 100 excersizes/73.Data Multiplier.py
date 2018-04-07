# Multiply the values of the text file in the URL by two and export the output to a new file
# url www.pythonhow.com/data/sampledata.txt

import pandas

data = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')
print(type(data))

data2 = data * 2
print(type(data2))

pandas.DataFrame.to_csv(data2, 'sampledata.txt', index=None)
