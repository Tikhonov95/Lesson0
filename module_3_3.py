def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(5)
print_params(5, 'новая строка')
print_params(5, 'новая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [10, 'список', False]
values_dict = {'a': 7, 'b': 'словарь', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
