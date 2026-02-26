from numpy.ma.core import maximum

names = ["Melina", "Erion","Egzon","Andi"]

for name in names:
    print(names)


sentence = "Hello World"

for character in sentence:
    if character.isalpha():
       print(character)


for number in range(1,9):
    print(number)


numbers = [12,45,78,89,56,23,14,47,25,58]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
        print("the biggest number in this list is : ",maximum)