def return_home():

    locations = []
    turns = []
    location = ""

    while location != "SCHOOL":

        turn = input()
        location = input()

        turns.append(turn)
        locations.append(location)

    locations.reverse()
    turns.reverse()

    for x in range(0, len(turns)):

        if turns[x] == "R":

            turns[x] = "L"

            continue

        if turns[x] == "L":

            turns[x] = "R"

            continue

    direction = []

    for x in turns:

        if x == "R":

            direction.append("RIGHT")

        if x == "L":

            direction.append("LEFT")

    for x in range(0, len(direction) - 1):

        print("Turn {dir} onto {location} street.".format(dir=direction[x], location=locations[x + 1]))

    return "Turn {dir} into your HOME.".format(dir=direction[len(direction) - 1])


print(return_home())
