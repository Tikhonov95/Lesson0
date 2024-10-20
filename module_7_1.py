class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return 'Файл не найден или пуст'

    def add(self, *products):
        existing_products = set()
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    name = line.split(', ')[0]
                    existing_products.add(name)
        except FileNotFoundError:
            pass

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(f'{str(product)}\n')
                    existing_products.add(product.name)
                else:
                    print(f'Продукт {product} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

s1.add(p1, p2, p3)
print(s1.get_products())