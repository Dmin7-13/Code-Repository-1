numpad = {"a":"2", "b":"2", "c":"2", "d":"3", "e":"3", "f":"3", "g":"4", "h":"4", "i":"4", "j":"5", "k":"5", "l":"5",
          "m":"6", "n":"6", "o":"6", "p":"7", "q":"7", "r":"7", "s":"7", "t":"8", "u":"8", "v":"8", "w":"9", "x":"9",
          "y":"9", "z":"9", "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}

number_of_phones = int(input())
list_of_numbers = []

for x in range(0, number_of_phones):

    number = input()

    list_of_numbers.append(number)

for x in range(0, len(list_of_numbers)):

    list_of_numbers[x] = list_of_numbers[x].replace("-", "")

for x in range(0, len(list_of_numbers)):

    if len(list_of_numbers[x]) > 10:

        list_of_numbers[x] = list_of_numbers[x][0:10]

print(list_of_numbers)

for x in range(0, len(list_of_numbers)):

   for i in range(0, len(list_of_numbers[x])):

        list_of_numbers[x] = list_of_numbers[x][i].replace(list_of_numbers[x][i], numpad[list_of_numbers[x][i]])

print(list_of_numbers)



