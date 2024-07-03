my_dict = {"Alex": 1995, "Yulia": 1990, "Daria": 2003}
print(my_dict)
print(my_dict["Alex"])
print(my_dict.get("Max"))
my_dict["Vladimir"] = 1998
my_dict["Kirill"] = 2000
a = my_dict.pop("Daria")
print(a)
print(my_dict)
my_set = [10, "Anton", "Anton", 20, 10]
my_set = set(my_set)
print(my_set)
my_set.add(15)
my_set.add((10,2,3))
my_set.remove(20)
print(my_set)

