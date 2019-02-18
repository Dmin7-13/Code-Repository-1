def comparison(val1, val2):

    if val1 > val2:

        return val1

    if val2 > val1:

        return val2

    if val1 == val2:

        return val1


num_computers = int(input())
computer_list = []

for x in range(0, num_computers):

    computer = input()

    computer_list.append(computer)

print(computer_list)
