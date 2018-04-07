# use Python to calculate the distance in kilometers between Jupiter and Sun on Jan
# 1st, 1230

import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
destance_au_units = jupiter.sun_distance
distance_km = destance_au_units * 149597870.691
print(distance_km)
