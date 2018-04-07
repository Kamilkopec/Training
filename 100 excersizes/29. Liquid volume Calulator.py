# write a function that calculates liquid volume in a sphere using the following formula.
# the radius is aways 10, so consider making it a default parameter

from math import pi


def liq_vol(h, r=10):
    a = ((4 * pi * r**3) / 3)-((pi * h**2 * (3 * r - h)) / 3)
    return a


print(liq_vol(2))
