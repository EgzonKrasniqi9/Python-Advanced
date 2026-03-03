


def person(name, greeting="Hello"):
    message= f"{greeting},{name}"
    return message
degault_greeting = person("Fetsa")
costum_greeting = person("Melina",'Hi')

print(degault_greeting)
print(costum_greeting)