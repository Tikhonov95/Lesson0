immutable_var = (5, 10,"Alex", False)
print(immutable_var)
# immutable_var[1] = 15;  Кортежи нельзя изменять, потому что они были разработаны таким образом.(из-за отсутствия выделенных элементов)
mutable_list = [20, 40, "Alex"]
print(mutable_list)
mutable_list[0] = 10
mutable_list[1] = 30
mutable_list[2] = "Alex1"
print(mutable_list)
