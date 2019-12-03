import math

input = open("input/3.txt", "r").read().split('\n')
maximum = 0

wire1 = input[0].split(',')
wire2 = input[1].split(',')


def add_steps(initial, direction, steps):
    wire_path = []
    global maximum
    for i in range(1, steps):
        if direction == 'R':
            wire_path.append([initial[0] - i, initial[1]])
        if direction == 'L':
            wire_path.append([initial[0] + i, initial[1]])
        if direction == 'D':
            wire_path.append([initial[0], initial[1] - i])
        if direction == 'U':
            wire_path.append([initial[0], initial[1] + i])
        last = wire_path[-1]
        maximum = max([maximum, abs(last[0]), abs(last[1])])
    return wire_path


def process_wire(wire):
    wire_path = [[0, 0]]
    for rule in wire:
        direction = rule[0]
        step = int(rule[1:])
        wire_path += add_steps(wire_path[-1], direction, step)
    return wire_path


wire_path1 = process_wire(wire1)[1:]
wire_path2 = process_wire(wire2)[1:]

center = maximum + 1
maximum = center * 2

my_map = [['[ ]'] * maximum for i in ['[ ]'] * maximum]
my_map[center][center] = '[o]'


def fill_map(point, cross):
    global my_map
    if my_map[point[0] + center][point[1] + center] != '[o]':
        my_map[point[0] + center][point[1] + center] = '[*]' if cross == 0 else '[$]'


def get_crossings_distance():
    distance = math.inf
    global my_map
    for point1 in wire_path1:
        fill_map(point1, 0)
        for point2 in wire_path2:
            fill_map(point2, 1)
            if point1[0] == point2[0] & point1[1] == point2[1]:
                # fill_map(point2, 1)
                temp_distance = abs(point1[0]) + abs(point1[1])
                distance = min(temp_distance, distance)

    return distance


print(get_crossings_distance())
text = '\n'.join(list(map(lambda x: ''.join(x), my_map)))

open("input/2.txt", "w").write(text)
