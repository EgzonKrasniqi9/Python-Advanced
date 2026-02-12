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