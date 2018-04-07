# concatenate 2 text file into a singe text file and print it.

import pandas

data = pandas.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data2 = pandas.read_csv('http://pythonhow.com/data/sampledata_x_2.txt')
# print(data2)
# print(data)

# final = data.append(data2, ignore_index=True)
# print(final)

datas = [data2, data]
final = pandas.concat(datas, ignore_index=True)
print(final)
pandas.DataFrame.to_csv(final, 'samplefinal.txt', index=None)


# print(type(data))
#
# data2 = data * 2
# print(type(data2))
#
# pandas.DataFrame.to_csv(data2, 'sampledata.txt', index=None)
