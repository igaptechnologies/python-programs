person = {
    "name":"Abhijit",
    "email":"gatadeabhijit@gmail.com"
}

print(person["name"])
print(person["email"])
person["email"] = "apg@gmail.com"
print(person)
person["gender"] = "Male"
print(person)
del person["email"]
print(person)
print(len(person))
print(person.keys())