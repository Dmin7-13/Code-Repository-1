from fractions import Fraction


def fraction_action():

    numerator = int(input("Numerator: \n"))

    denominator = int(input("Denominator: \n"))

    fraction = Fraction(numerator, denominator)

    return fraction

  
print(fraction_action())
