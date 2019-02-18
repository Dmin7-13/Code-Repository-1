def sum_to_ten():

    die1 = int(input())
    die2 = int(input())

    if die1 > 9:

        die1 = 9

    if die2 > 9:

        die2 = 9

    correct = 0

    for x in range(1, die1 + 1):

        for i in range(1, die2 + 1):

            if x + i == 10:

                correct += 1

    total = "There are " + str(correct) + " ways to get the sum 10."

    if correct == 1:

        total = "There is 1 way to get the sum 10."

    return total

print(sum_to_ten())