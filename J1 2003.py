import math


def calc_width(space):

    val = space

    return val


def print_tines(width, tine_len):

    space = ""

    for x in range(0, width):

        space += " "

    for x in range(0, tine_len):

        print("*{space}*{space}*".format(space=space))

    return


def print_flat(width):

    flat = ""

    for x in range(0, width * 2 + 3):

        flat += "*"

    print(flat)

    return


def print_handle(width, handle_len):

    space = ""

    for x in range(0, width + 3 // 2):

        space += " "

    for x in range(0, handle_len):

        print("{space}*".format(space=space))

    return


tines = int(input())
spacing = int(input())
handle = int(input())
width = calc_width(spacing)

print_tines(width, tines)
print_flat(width)
print_handle(width, handle)

