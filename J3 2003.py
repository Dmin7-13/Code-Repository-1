def snakes_ladders():

    pos = 0

    while pos != 100:

        roll = int(input())

        pos += roll

        if roll == 0:

            return "You Quit!"

        if pos == 54:

            pos = 19

        if pos == 90:

            pos = 48

        if pos == 99:

            pos = 77

        if pos == 9:

            pos = 34

        if pos == 40:

            pos = 64

        if pos == 67:

            pos = 86

        if pos > 100:

            pos -= roll

        print("You are now on square {sqr}".format(sqr=pos))

        if pos == 100:

           return "You win"


print(snakes_ladders())