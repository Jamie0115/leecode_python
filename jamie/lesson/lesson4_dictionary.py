#  dictionary = {key, value}
person = {
    "name": "Jamie",
    "age": 25
}
print(person["name"])
print(person.get("name"))

person["name"] = "Eren"
print(person)

person["country"] = "TW"
print(person)

del person["age"]
print(person)