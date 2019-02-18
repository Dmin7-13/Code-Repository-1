def amr_to_cdn(word):

    if len(word) < 64:

        if word[-3].lower() not in "aeiouy" and word[len(word) - 2:len(word)].lower() == "or" and len(word) > 3:

            word = word[:-1] + "u" + word[-1:]

        return word

    else:

        return "The length of the string must be under 64 characters"


word = input()

while word != "quit!":

    print(amr_to_cdn(word))

    word = input()
