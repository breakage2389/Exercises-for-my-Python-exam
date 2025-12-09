# class NumList:
#     def __init__(self, data):
#         self.values = [x for x in data if isinstance(x, (int, float))]
#
#     def show(self):
#         print(self.values)
#
#     def avg(self):
#         if not self.values:
#             return None
#         return sum(self.values) / len(self.values)
#
#
# nums = NumList([1, "a", 3.5, None, 7, [], 2])
# nums.show()
# print(nums.avg())
from curses.ascii import isdigit


# 4зад. Дефинирайте клас Shape с едно поле задаващо вида на фигурата.
# Дефинирайте клас Square и клас Circle,които наследяват Shape.
# Класьт Square и класьт Circle имат предефинирана функция _init_
# която приема длжина(радиус) като аргумент. И трите класа имат метод за намиране на лице,като лицето на Shape e 0 по подразбиране. Потребителя вьвежда вида на фигурата и на тази база се
# създава обект от съответния клас.
# След това се извиква метода за намиране на лице за съответния обект.
# Добавете обработка на изключения.

# class Shape:
#     def __init__(self, figure):
#         self.figure = figure
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, side : float):
#         super().__init__(figure)
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
# class Circle(Shape):
#     def __init__(self, radius :float):
#         super().__init__(figure)
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius *3.14
#
# try:
#     figure = input("Въведи фигура (square/circle): ").strip().lower()
#
#     if figure == "square":
#         value = float(input("Въведи страна: "))
#         obj = Square(value)
#
#     elif figure == "circle":
#         value = float(input("Въведи радиус: "))
#         obj = Circle(value)
#
#     else:
#         raise ValueError("Непозната фигура.")
#
#     print("Лице:", obj.area())
#
# except ValueError as e:
#     print("Грешка:", e)
#
# except Exception:
#     print("Възникна неочаквана грешка.")

# zad 6 NIKOLAY
# - Ура, можете да построите триьгьлник!
# - Нищо няма да работи с отрицателни числа!
# - Трябва да введете само числа!
# - Жалко, но не можете да направите тригьлник от това !
# Дефинирайте метод get_triangle_type(), който връща като резултат типа на триььлника :
# равностранен, равнобедрен или разностранен
# class TriangleChecker:
#     def __init__(self, a, b, c):
#
#         if not all(isinstance(x, (int, float)) for x in (a, b, c)):
#             self.valid = False
#             self.message = "Трябва да введете само числа!"
#             return
#         self.a, self.b, self.c = a, b, c
#         self.valid = True
#
#     def is_triangle(self):
#         if not self.valid:
#             return False
#
#         if self.a <= 0 or self.b <= 0 or self.c <= 0:
#             self.message = "Нищо няма да работи с отрицателни числа!"
#             return False
#
#         if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             self.message = "Ура, можете да построите триъгълник!"
#             return True
#         else:
#             self.message = "Жалко, но не можете да направите триъгълник от това !"
#             return False
#
#     def get_triangle_type(self):
#         if not self.is_triangle():
#             return self.message
#
#         if self.a == self.b == self.c:
#             return "равностранен"
#         elif self.a == self.b or self.a == self.c or self.b == self.c:
#             return "равнобедрен"
#         else:
#             return "разностранен"
#
# t1 = TriangleChecker(5, 5, 5)
# print(t1.get_triangle_type())  # равностранен
#
# t2 = TriangleChecker(5, 5, 3)
# print(t2.get_triangle_type())  # равнобедрен
#
# t3 = TriangleChecker(3, 4, 5)
# print(t3.get_triangle_type())  # разностранен
#
# t4 = TriangleChecker(1, 2, 10)
# print(t4.get_triangle_type())  # Жалко, но не можете да направите триъгълник от това !
#
# t5 = TriangleChecker("a", 2, 3)
# print(t5.get_triangle_type())  # Трябва да введете само числа!
#
# t6 = TriangleChecker(-1, 2, 2)
# print(t6.get_triangle_type())  # Нищо няма да работи с отрицателни числа!


#zad7
# class Food:
#     def __init__(self , carbs , protein , fat):
#         self.carbs = carbs
#         self.protein = protein
#         self.fat = fat
#
#
#     def calories(self):
#         print(4 * self.carbs + 4* self.protein +9 * self.fat)
#         return 4 * self.carbs + 4* self.protein +9 * self.fat
#
# class Recipe:
#     def __init__(self, name, ingredients):
#         if not ingredients:
#             raise ValueError("Рецептата трябва да има поне един продукт.")
#         self.name = name
#         self.ingredients = ingredients
#
#     def calories(self):
#         return sum(food.calories() for food in self.ingredients)
#
#     def __str__(self):
#         return self.name
#
#
# def get_positive_int(prompt, min_value, max_value):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value < min_value or value > max_value:
#                 raise ValueError
#             return value
#         except ValueError:
#             print(f"Моля, въведете цяло число между {min_value} и {max_value}.")
#
#
# num_recipes = get_positive_int("Въведете брой рецепти (5-14): ", 5, 14)
#
# recipes = []
#
# for i in range(num_recipes):
#     name = input(f"Въведете име на рецепта {i+1}: ")
#     ingredients = []
#     while True:
#         try:
#             n = int(input(f"Колко съставки има рецептата '{name}'? "))
#             if n <= 0:
#                 raise ValueError
#             break
#         except ValueError:
#             print("Моля, въведете положително цяло число за броя на съставките.")
#
#     for j in range(n):
#         print(f"Съставка {j+1}:")
#         while True:
#             try:
#                 carbs = float(input("Въглехидрати (г): "))
#                 protein = float(input("Протеин (г): "))
#                 fat = float(input("Мазнини (г): "))
#                 ingredient = Food(carbs, protein, fat)
#                 ingredients.append(ingredient)
#                 break
#             except ValueError as e:
#                 print(f"Грешка: {e}. Опитайте отново.")
#
#     recipe = Recipe(name, ingredients)
#     recipes.append(recipe)
#
#
# for recipe in recipes:
#     print(f"Рецепта: {recipe}, Калории: {recipe.calories()}")
