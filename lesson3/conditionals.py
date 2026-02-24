from PIL.ImImagePlugin import number

age = 18

if age >= 18:
    print("You cant vote.")
else:
    print("You cannot vote yet.")


temperature = 28
if temperature > 36:
    print("It's hot day, stay haydrated")
elif  20<=temperature <=30:
    print("The weather is pleasant")
else:
    print("It's a cold day")

number = 7

if number %2 ==0:
    print("the number is even")
else:
    print("The number is odd")