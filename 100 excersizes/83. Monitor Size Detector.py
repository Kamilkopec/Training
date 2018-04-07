# write a script that detects and prints out your monitor resolution

from win32api import GetSystemMetrics

print('wight = {}, height = {}'.format(GetSystemMetrics(0), GetSystemMetrics(1)))

# z udemy

# pip install screeninfo

from screeninfo import get_monitors

w = get_monitors()[0].width
h = get_monitors()[0].height

print('w = {}, h = {}'.format(w, h))