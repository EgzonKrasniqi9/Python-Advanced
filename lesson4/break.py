from typing_inspection.typing_objects import target

numbers = [1,2,3,4,5,6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found!")
        break