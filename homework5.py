immutable_var = (5, 10,"Alex", False)
print(immutable_var)
# immutable_var[1] = 15 (из-за отсутствия выделенных элементов)
mutable_list = (5, [10,"Alex"], False)
print(mutable_list)
mutable_list[1][1] = 15
print(mutable_list)