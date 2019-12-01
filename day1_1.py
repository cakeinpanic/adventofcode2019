import math
import re
from functional import seq

input = seq(open("input/1.txt", "r")) \
    .map(lambda x: re.match(r'(\d+)', x)[0]) \
    .map(lambda x: int(x))\
    .to_list()

result = 0

for module in input:
    fuel = math.floor(module / 3) - 2
    if fuel > 0:
        result += fuel
        input.append(fuel)



print(result)
