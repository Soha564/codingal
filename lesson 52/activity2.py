dictionary = {}

dictionary = {1 : "apple", 2 : "banana"}

dictionary = {"name":"John", 1: [1, 2, 4]}

dictionary = {"name":"jack", "age": 26}

print(dictionary["name"])
print(dictionary.get("age"))

dictionary["age"] = 27
print(dictionary)

dictionary["address"] = "Downtown"
print(dictionary)

dictionary.pop("age")
print(dictionary)

print("Address: ", dictionary.get("address"))

dictionary.clear()
print("Cleared dictionary: ", dictionary)