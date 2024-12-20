from pprint import pprint

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        listing = open(self.__file_name, 'r')
        product = listing.read()
        listing.close()
        return product

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for product in products:
            if str(product) in self.get_products():
                print(f'Продукт {str(product)} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
        file.close()

class Product(Shop):
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())