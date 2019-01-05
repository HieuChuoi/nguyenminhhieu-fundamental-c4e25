person = {
    "Name": "Quan",
    "Age": 25,
    "Location": "Hanoi",
    "Exes": 3,
    "Status": False,
    "Friends": 125,
}

# person["Name"] = "A.Quan"  #update


# print(person["Location"])
# print(person["Exes"])
# print(person["Status"])
# print(person["Friends"])

# person["Exp"] = 2   #create
# print(person)

# if "Name" in person:
#     print("Exits")
# else:
#     print("Not Exits")

del person["Exes"]
print(person)