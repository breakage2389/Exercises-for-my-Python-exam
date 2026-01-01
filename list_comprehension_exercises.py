#1. Филтриране на скъпи продукти
#Имаш списък с цени. Трябва да извлечеш само тези, които са над средната цена.
# Задача: Създай списък expensive_prices, който съдържа само сумите над 50.00.
#resheniee
# prices = [10.50, 120.0, 45.0, 90.0, 5.20]
# expensive_prices = [x for x in prices if x >50]
from selectors import SelectSelector

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
class Market:
    def __init__(self, barcod, name, manufacturer, price, quantity):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

nike_products = [
    Market(1001, "Air Max 270", "Nike", 280.00, 10),
    Market(1002, "Revolution 6", "Nike", 45.00, 25),
    Market(1003, "Downshifter 12", "Nike", 25.00, 3),
    Market(1004, "Jordan Low", "Nike", 210.00, 5),
    Market(1005, "Court Vision", "Nike", 35.00, 20)
]
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

# 1. Филтър за дължина на думи
# Вход: words = ["apple", "it", "python", "ai", "banana", "code"]
# Задача: Създай списък само с думите, които са по-дълги от 3 символа.
#reshenie
# words = ["apple", "it", "python", "ai", "banana", "code"]
# l1st = [x for x in words if len(x) >3]
# print(l1st)

# 2. Числата в стрингове
# Вход: numbers = [1, 5, 10, 15]
# Задача: Превърни списъка в стрингове, но добави "лв." след всяко число (напр. "1 лв.").
# numbers = [1, 5, 10, 15]
# l1st = [f'{str(x)}лв.' for x in numbers ]
# print(l1st)

# 3. Търсене на буква
# Вход: fruits = ["apple", "cherry", "banana", "kiwi", "mango"]
# Задача: Направи списък само от плодовете, които съдържат буквата "a".
# fruits = ["apple", "cherry", "banana", "kiwi", "mango"]
# l1st = [x for x in fruits if 'a' in x.lower()]
# print(l1st)
#################### po-trudni primeri
# 4. Обратни числа
# Вход: nums = [1, -2, 3, -4, 5]
# Задача: Създай списък, в който положителните числа стават отрицателни, а отрицателните — положителни.
# nums = [1, -2, 3, -4, 5]
# l1st = [-x for x in nums]
# print(l1st)

# 5. Филтър "Кратни на 3 и 5"
# Вход: range(1, 51)
# Задача: Извлечи само числата, които се делят едновременно на 3 и на 5.
# l1st = [x for x in range(1,51) if x % 3 == 0 if x % 5 == 0]
# print(l1st)

# 6. Намиране на индекси
# Вход: letters = ["a", "b", "c", "d"]
# Задача: Използвай enumerate() в list comprehension, за да получиш списък от тупли (индекс, елемент).
# letters = ["a", "b", "c", "d"]
# l1st = [(idx,el) for idx,el in enumerate(letters)]
# print(l1st)

################################ oshte po-trudni
# 7. "Elif" категоризация на цени
# Вход: prices = [5, 15, 60, 120, 8]
# Задача: Създай списък със статуси: "Cheap" (под 10), "Normal" (10-50), "Expensive" (над 50).
# prices = [5, 15, 60, 120, 8]
# l1st = [
#     'cheap' if x <10 else
#     'normal' if 10<=x <= 50 else
#     'expensive' for x in prices
# ]
# print(l1st)

# 8. Филтриране на обекти по име
# Вход: Използвай твоя списък nike_products.
# Задача: Извлечи обектите (целите обекти!), чието име съдържа думата "Air".
# l1st = [x for x in nike_products if 'Air' in x.name]
# for i in l1st:
#     print(i.barcod, i.name, i.quantity , i.price , i.quantity)


# 9. Списък от речници
# Вход: nike_products.
# Задача: Създай списък, където всеки елемент е речник с ключове "n" (за името) и "p" (за цената).
# Пример: [{"n": "Air Max", "p": 250}, ...]
# l1st = [{'n' : x.name , 'p' : x.price} for x in nike_products]
# for item in l1st:
#     print(item)


# 10. "Flatten" на матрица с филтър
# Вход: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Задача: Направи списък от всички числа в матрицата, но само ако са четни.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l1st = [num for row in matrix for num in row if num %2 ==0 ]

# 11 От списък с цени в лева върни само тези над 100, намалени с 20%.
# prices = [50, 120, 80, 200, 150]
# prices = [(x-x*(2/10)) for x in prices if x >100]
# print(prices)

# 12 От списък с думи върни само тези с дължина ≥ 5, в uppercase.
# words = ["apple", "kiwi", "banana", "fig", "orange"]
# words = [x.upper() for x in words if len(x)> 5]
# print(words)

#13 Върни всички елементи на четни позиции, умножени по индекса им.
# nums = [3, 5, 7, 9, 11]
# nums = [nums[i]*i  for i in range(len(nums)) if i%2==0]
# print(nums)

#14 От списък с числа върни:x*x ако е четно ;x ако е нечетно
# nums = [1, 2, 3, 4, 5]
# nums = [x*x if x%2==0 else x for x in nums]
# print(nums)

# 155. Вложен list comprehension.От матрица върни само четните числа, сплескани в един списък.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = [x for row in matrix for x in row if x%2==0 ]
print(matrix)