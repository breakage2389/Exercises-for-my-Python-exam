"""
УСЛОВИЕ НА ЗАДАЧАТА:
1. Въвеждане на данни:
   - Въвеждат се две цели положителни числа: N (брой елементи) и K (критерий).
   - Въвежда се списък 'nums' от N цели числа.

2. Обработка на списък 1 (nums1):
   - Филтрират се всички числа от 'nums', които са по-големи от K.
   - Намира се произведението на елементите на НЕЧЕТНИ позиции (индекси 1, 3, 5...) в 'nums1'.
   - Намира се индексът на най-малкия елемент в 'nums1'.

3. Обработка на списък 2 (nums2):
   - Филтрират се числата от 'nums', които са по-малки или равни на K, но са положителни (> 0).
   - Намира се разликата между най-големия и най-малкия елемент в 'nums2'.

4. Валидация:
   - Функцията input_number гарантира, че N и K са положителни, а за X позволява и отрицателни стойности.
"""
# import random
# while True:
#     try:
#         n = int(input('n:'))
#         k = int(input('k:'))
#         if n > 0 and k > 0:
#             break
#     except ValueError:
#         print('Value error')
#         continue
#     except Exception as e:
#         print(e)
#         continue
#
# nums  =[]
# nums1 = []
# for i in range(n):
#     nums.append(random.randint(1, 50))
# print(nums)
#
# for i in nums:
#     if i <= k: #ako chislo e po-malko ot k go maha ili kakto e tuk ako i e po-malko ili ravno go dobavq
#         nums1.append(i)
# print(nums1)
#
# nums1_uneven =nums1[1::2] #necheten index only
# storage = 1
# for num1 in nums1_uneven:
#     storage *= num1
# print(storage)
#
# #za namiraneto edin nachin e ako ordernem lista i nums1[0] vinagi shte bude nai-malkiq el
# # nums1.sort()
# # print(f'nai-malkiq el e {nums1[0]}')
#
# min_value = min(nums1)
# min_index = nums1.index(min_value)
#
# # list 2 -> nums2
#
# nums2 = [i for i in nums if i >0]
# print(f'Razlikata v nums2 e ->{max(nums2) - min(nums2)}')


# zad 2
# Създайте клас Book, който съдържа следната информация за всяка книга:
# Име (book_name)
# Уникален код (book_code)
# Цена (book_price)
# Година на издаване (book_year)
# Автор (book_author)
#def func (INFO -> ime ,code , cena , god, avtor
#def sortbyname
# Функция за сортиране от Я -> А
# Функция за филтриране по автор , ако няма не принтваме нищо
#Функция за търсене по код: godina na izdawane

class Book:
    def __init__(self, book_name , book_code , book_price , book_year , book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'{self.book_name , self.book_code, self.book_price, self.book_year, self.book_author}'

    def __lt__(self, other):
        return self.book_name < other.book_name

books = [
    Book('A1', 121, 12.34, 2022, 'BC'),
    Book('A1', 124, 34.22, 2021, 'BB'),
    Book('A2', 125, 20, 2022, 'BC'),
    Book('A3', 120, 7.43, 2021, 'AC'),
]

def reverse_sort(books):
    return books[::-1]

def sort_author(books,author):
    for i in books:
        if i.book_author == author:
            print(i)

def code(books,target_code ):
    for book in books:
        if book.book_code == target_code:
            print(book.book_year)
            return
        else:
            print('not found')



# 1. Сортиране и принтиране
# Тъй като reverse_sort връща списък, трябва да го обходим, за да видим книгите
print("--- Сортиране Я-А ---")
sorted_books = reverse_sort(books)
for b in sorted_books:
    print(b)

# 2. Търсене по автор
# Внимавай: 'BC' съществува, 'XY' не – за 'XY' просто няма да изпише нищо (както е по условие)
print("\n--- Търсене на автор 'BC' ---")
sort_author(books, 'BC')

print("\n--- Търсене на автор 'XY' (очакваме празно) ---")
sort_author(books, 'XY')

# 3. Търсене по код
# Тук оправих логиката с 'else', за да не принтира "not found" на всяка стъпка
def code(books, target_code):
    for book in books:
        if book.book_code == target_code:
            print(f"Намерен код {target_code}, година: {book.book_year}")
            return # Спираме веднага щом намерим книгата
    print(f'Code {target_code}: not found') # Само ако цикълът свърши без успех

print("\n--- Тест на кодове ---")
code(books, 121) # Съществува
code(books, 119) # Не съществува