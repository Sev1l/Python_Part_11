## More comprehensions
# Task 2 (Products in shopping list)


class ShoppingList:
    def __init__(self):
        self.products = []   

    def add(self, name, quantity):
        self.products.append((name, quantity))

    def __iter__(self):
        self.index = 0       
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product

def products_in_shopping_list(shopping_list,amount):
    return [item[0] for item in shopping_list if item[1] >= amount]


my_list = ShoppingList()
my_list.add("bananas", 10)
my_list.add("apples", 5)
my_list.add("alcohol free beer", 24)
my_list.add("pineapple", 1)

print("the shopping list contains at least 8 of the following items:")
for product in products_in_shopping_list(my_list, 8):
    print(product)
