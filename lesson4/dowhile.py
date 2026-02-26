while True:
    user_input= input("Enter a positive nuber: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break

    print("Invalid input. Please try again.")

print("You entered a valid positive number whitch is: ",number)