def similes():

    num_adjectives = int(input())
    num_nouns = int(input())
    adjective_list = []
    noun_list = []

    for x in range(0, num_adjectives):

        adjective = input()

        adjective_list.append(adjective)

    for x in range(0, num_nouns):

        noun = input()

        noun_list.append(noun)

    for x in adjective_list:

        for i in noun_list:

            simile = str("{adj} as {noun}".format(adj=x, noun=i))

            print(simile)

    return ""

print(similes())
