# please download zip file and extract its file in a folder.
# write a scrpt that counts and prints out  the number of .py files in that folder

import glob

dir = r'D:\Projekty Python\Training\Udemy\100 Python Excersizes\files'
pyCounter = glob.glob1(dir, '*.py')
print(len(pyCounter))