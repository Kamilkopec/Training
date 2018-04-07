# download zip. inside the zip file is a directory named subdirs
# that directory contains other directories inside.
# please write a script that count the number of .py files contained
# inside subdirs and all its sub-directories.

import glob

dir = r'D:\Projekty Python\Training\Udemy\100 Python Excersizes\subdirs'
pyCounter = glob.glob(dir + '/**/*.py', recursive=True )

print(len(pyCounter))
