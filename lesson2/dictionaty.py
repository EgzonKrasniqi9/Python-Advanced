contact_info ={"Festa": "123-465",
               "Egzon": "7789-546"
}

festa_phone = contact_info["Festa"]
print(festa_phone)

contact_info["Festa"]= "123-123"
print(contact_info)
contact_info["Melina"]= "111-222"
print(contact_info)

del contact_info["Egzon"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {

    "Festa":{
        "phone_number" : "123-456",
        "email" : "sara@gmail.com",
        "home_address" : "Bregu i Diellit",
        "birthday" : "24/12/2007"
    },
    "Melina":{
        "phone_number" : "789-465",
        "email" : "melina@gmail.com",
        "home_address" : "Taslixhe",
        "birthday" : "27/09/2008"
    }
}

print(contact_information)

sara_information = contact_information["Festa"]
print(sara_information)

contacts = {
    "Festa":("123-456", "festa@gmail.com"),
    "Melina":("789-456", "melina@gmail.com"),
}

festa_info = contacts["Festa"]
phone_number = festa_info[0]
print(phone_number)

phone_number, email = contacts["Festa"]