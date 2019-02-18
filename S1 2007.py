birthdays = int(input())
birthday_list = []

for x in range(0, birthdays):

    birth = input()

    birthday_list.append(birth.split())

for x in birthday_list:

    if int(x[0]) < 1989 or (int(x[0]) <= 1989 and int(x[1]) < 2) or (int(x[0]) <= 1989 and int(x[1]) <= 2 and int(x[2]) <= 27):

        print("Yes")

    else:

        print("No")