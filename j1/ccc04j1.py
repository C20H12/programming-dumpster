from math import sqrt
from math import floor


tiles = int(input())
sideLength = floor(sqrt(tiles))
print("The largest square has side length {}.".format(sideLength))
