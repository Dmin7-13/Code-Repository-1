num_of_words = int(input())

word_list =[]

for x in range(0, num_of_words):

    word_possibility = []
    final_possibility = []
    word = input()

    word_list.append(word)

    for i in range(0, len(word_list[x])):

        for a in range(0, len(word_list[x]) + 1):

            word_possibility.append(word_list[x][i:a])

    for i in word_possibility:

        if word_possibility.count(i) > 1:

            continue

        final_possibility.append(i)

    print(final_possibility)





