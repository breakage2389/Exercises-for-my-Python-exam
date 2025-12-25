#1. Филтриране на скъпи продукти
#Имаш списък с цени. Трябва да извлечеш само тези, които са над средната цена.
# Задача: Създай списък expensive_prices, който съдържа само сумите над 50.00.
#resheniee
# prices = [10.50, 120.0, 45.0, 90.0, 5.20]
# expensive_prices = [x for x in prices if x >50]

# 2. Трансформация на имена (Upper case)
# Това е често срещано при обработка на данни от потребителски вход.
# Вход: names = ["nike air", "adidas samba", "puma runner"]
# Задача: Създай нов списък, в който всяко име е с главни букви.
#resheniee
# names = ["nike air", "adidas samba", "puma runner"]
# upper_names = [x.title() for x in names ]
# print(upper_names)

# 3. "Магическо" филтриране на четни числа (с логика)
# Вход: numbers = range(1, 21)
# Задача: Направи списък, който съдържа квадратите само на четните числа.
# Очакван резултат: [4, 16, 36, ...]
#resheniee
# numbers = range(1, 21)
# l_god = [x**2 for x in numbers if x % 2 == 0]
# print(l_god)

# 4. Усложнена задача: Търсене в обекти (Свързана с  клас Market) ;имаш списъка nike_products.
# Задача: Използвай list comprehension, за да извлечеш само имената на продуктите,
# чиято наличност (quantity) е по-малка от 10.
#resheniee
# class Market:
#     def __init__(self, barcod, name, manufacturer, price, quantity):
#         self.barcod = barcod
#         self.name = name
#         self.manufacturer = manufacturer
#         self.price = price
#         self.quantity = quantity
#
# nike_products = [
#     Market(1001, "Air Max 270", "Nike", 280.00, 10),
#     Market(1002, "Revolution 6", "Nike", 45.00, 25),
#     Market(1003, "Downshifter 12", "Nike", 25.00, 3),  # < 10
#     Market(1004, "Jordan Low", "Nike", 210.00, 5),     # < 10
#     Market(1005, "Court Vision", "Nike", 35.00, 20)
# ]
# l1 = [x.name for x in nike_products if x.quantity < 10 ]
# for z in l1:
#     print(z)

# 5. Задача с If-Else (Ternary Operator)
# Задача: Имаш списък с количества: quantities = [5, 0, 12, 3, 0].
# Условие: Създай нов списък със стрингове:
# ако количеството е 0, сложи "Out of stock", в противен случай сложи "Available".
#resheniee
# quantities = [5, 0, 12, 3, 0]
# string_list = ['Out of stock' if x == 0 else 'Available' for x in quantities]
# print(string_list)

# dopulnitelna zadacha
# import random
# spisuk = [random.randint(1, 100) for _ in range(25)]
#
# l1st = [
#     'stoinost nad 50' if x >50 else
#     'stoinost nad 25  x >25' if x >25 else
#     'stoinost x <= 25 '
#     for x in spisuk
# ]
# print(l1st)