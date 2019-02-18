def middle_bowl():

    w1 = int(input())
    w2 = int(input())
    w3 = int(input())

    weight_list = [w1, w2, w3]

    middle = sorted(weight_list)

    middle = middle[1]

    return middle

print(middle_bowl())
