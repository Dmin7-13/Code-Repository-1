def txt_translate(word):

    if word == "CU":

        return "see you"

    elif word == ":-)":

        return "i'm happy"

    elif word == ":-(":

        return "i'm unhappy"

    elif word == ";-)":

        return "wink"

    elif word == ":-P":

        return "stick out my tongue"

    elif word == "(~.~)":

        return "sleepy"

    elif word == "TA":

        return "totally awesome"

    elif word == "CCC":

        return "Canadian Computing Competition"

    elif word == "CUZ":

        return "because"

    elif word == "TY":

        return "thank-you"

    elif word == "YW":

        return "you're welcome"

    elif word == "TTYL":

        return "talk to you later"

    return word


string = ""

while string != "TTYL":

    string = input()

    print(txt_translate(string))
