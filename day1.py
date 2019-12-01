import math
import re
from functional import seq

result = seq(open("input/1.txt", "r"))\
    .map(lambda x: re.match( r'(\d+)', x)[0])\
    .map(lambda x: int(x))\
    .map(lambda x: math.floor(x / 3) - 2)\
    .reduce(lambda x, y: x + y)

print(result)

