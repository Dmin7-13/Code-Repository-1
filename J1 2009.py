isbn = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

loop_count = 0

while loop_count < 3:

    num = int(input())

    isbn.append(num)

    loop_count += 1

count = 0

for x in range(0, len(isbn)):

    if count % 2 == 1:

        isbn[x] *= 3

    count += 1

isbn_val = 0

for x in range(0, len(isbn)):

    isbn_val += isbn[x]

print("The 1-3-sum is " + str(isbn_val))
