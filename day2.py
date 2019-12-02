import math
import re
from functional import seq

input = seq(open("input/2.txt", "r"))[0].split(',')
input = seq(input).map(lambda x: int(x)).to_list()

input[1] = 12
input[2] = 2

step = 4
i = 0

while i < len(input) - step:
    a = input[input[i + 1]]
    b = input[input[i + 2]]
    c = 0
    newPosition = input[i + 3]
    if input[i] == 1:
        c = a + b
    if input[i] == 2:
        c = a * b

    input[newPosition] = c
    i += step

print(input[0])
