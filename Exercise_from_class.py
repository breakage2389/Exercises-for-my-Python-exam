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