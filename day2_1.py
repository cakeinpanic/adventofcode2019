from functional import seq

global_input = seq(open("input/2.txt", "r"))[0].split(',')
global_input = seq(global_input).map(lambda x: int(x)).to_list()

step = 4


def get_input(a, b):
    new_input = global_input[:]
    new_input[1] = a
    new_input[2] = b

    return new_input


def get_result(input):
    i = 0

    while i < len(input) - step:
        a = input[input[i + 1]]
        b = input[input[i + 2]]
        c = 0
        new_position = input[i + 3]
        if input[i] == 1:
            c = a + b
        if input[i] == 2:
            c = a * b

        input[new_position] = c
        i += step

    return input[0]


def get_pair():
    for a in range(99):
        for b in range(99):
            if get_result(get_input(a, b)) == 19690720:
                return 100 * a + b


print(get_pair())
