word1 = input()
word2 = input()

word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

if sorted(word1) == sorted(word2):

    print("Is an anagram.")

else:

    print("Is not an anagram.")