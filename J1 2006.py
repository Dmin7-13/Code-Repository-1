def burger():

    choice = int(input())
    total = 0

    if choice == 1:

        total += 461

    if choice == 2:

        total += 431

    if choice == 3:

        total += 420

    return total


def sides():

    choice = int(input())
    total = 0

    if choice == 1:

        total += 100

    if choice == 2:

        total += 57

    if choice == 3:

        total += 70

    return total


def drink():

    choice = int(input())
    total = 0

    if choice == 1:

        total += 130

    if choice == 2:

        total += 160

    if choice == 3:

        total += 118

    return total


def desserts():

    choice = int(input())
    total = 0

    if choice == 1:

        total += 167

    if choice == 2:

        total += 266

    if choice == 3:

        total += 75

    return total


total = burger() + sides() + drink() + desserts()

print("Your total Calorie count is {calories}.".format(calories=total))