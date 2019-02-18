weight = float(input())
height = float(input())

bmi = weight/ height ** 2

health = "Normal weight"

if bmi < 18.5:

    health = "Underweight"

if bmi > 25:

    health = "Overweight"

print(health)