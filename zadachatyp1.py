#izpit po vuvedenie v programiraneto var 1
#n = 25 <= n <= 45 // while True : -> try except prowerka
#lst_1 = s 'n' na broi el ,  interval (p;q )
# p e random int ot -3700 , -1600 ,  q = 2222 do  3333
#broi na el >0 from lst_1 % 6 == 3
#lst_2 posle

import random

# while True:
#     try:
#         n = int(input('25<= n <=45'))
#         if 25 <= n <= 45:
#             break
#     except ValueError:
#         print('Trqbwa da bude int  (25<= n <=45), gledai da ne e bukwa')
#         continue
#     except Exception as e:
#         print(e)
#         continue





#tuk shte go prawq s n=5 zashto prowerkata shte bude muchenie.. :*(
# n = 5
# p = random.randint(-3700,-1600)
# q = random.randint(2222 ,  3333)
#
# lst_1 = []
# print(f'Intervala e {p} do {q} vkluchitelno')
#
# for i in range(n):
#     i = int(input('dobawi chislo'))
#     if p <= i <= q:
#         lst_1.append(i)
#     else:
#         print(f'chislto trqbwa da e v interwala -> [{p} ; {q}]')
#
# print(lst_1)
# count=0
# for i in lst_1:
#     if ((i //100)%10) % 2 == 0:
#         count += 1
# print(f'broq e ->{count}')
#
# min_value= float('inf')
# min_index = -1
# for i , y in enumerate(lst_1):
#     if y % 6 ==3:
#         if y < min_value:
#             min_value = y
#             min_index = i
# print(min_index , min_value)
#

# lst_1 = [-25, 21 ,4,5 , 25 ,75, 50 ,125]
# lst_2 = []
# for num in lst_1:
#     if 10<= num <= 99 or -99<= num <=-10:
#         if num % 5 ==0:
#             lst_2.append(num)
# print(lst_2)


# collector = 1
# odd_lst_2 = lst_2[1::2]
# for i in odd_lst_2:
#     collector *= i
# print(collector)

# lst_2 = [num for i, num in enumerate(lst_2) if not (i % 2 != 0 and num % 2 == 0)]
# print(lst_2)
#
# if len(lst_2) == len(lst_1):
#     print('fine sa')
# elif len(lst_2) < len(lst_1): #l2= [1,2,3,4]
#     sreda = len(lst_2)//2
#     novochislo = lst_2[0] * lst_2[-1]
#     lst_2.insert(sreda, novochislo)
# elif len(lst_1) > len(lst_2):
#     sreda = len(lst_1) // 2
#     novochislo = lst_1[0] * lst_1[-1]
#     lst_1.insert(sreda, novochislo)

#zad2
class Market:
    def __init__(self , barcod , name , manufacturer , price , quantity ):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def sale(self, quantity):
        self.quantity -= quantity
        return self.quantity

    def discount(self):
        if 30 <= self.price <= 50:
            discount_value = self.price * 0.05
            self.price -= discount_value
        elif 10 <= self.price <= 29:
            discount_value = self.price * 0.07
            self.price -= discount_value
        else:
            # Ако цената е над 50 или под 10, няма отстъпка
            pass
        return self.price
# n= int(input('N: '))
# product_list = []
# for i in range(n):
#     print('Product number -> ',i+1)
#     barcod = int(input('Barcod: '))
#     name = input('Name: ')
#     manufacturer = input('Manufacturer: ')
#     price = float(input('Price: '))
#     quantity = int(input('Quantity: '))
#     new_product = Market(barcod , name , manufacturer , price, quantity)
#     new_product.discount()
#     product_list.append(new_product)
#
# print("\n--- Product Inventory ---")
# for product in product_list:
#     print(f'barcode ={product.barcod} name = {product.name} , manufacturer = {product.manufacturer} ,'
#           f' price = {product.price}, quantity = {product.quantity}')
#
# def search_by_barcod(product_list , barcod):
#     for code in product_list:
#         if code.barcod == barcod:
#             print(f'barcode ={code.barcod} name = {code.name} , manufacturer = {code.manufacturer} ,'
#                   f' price = {code.price}, quantity = {code.quantity}')
#         else:
#             print('Wrong barcode!!!')
#
# print('*************')
# search_by_barcod(product_list , 30)

nike_products = [
    Market(1001, "Air Max 270", "Nike", 280.00, 3),
    Market(1002, "Revolution 6", "Nike", 45.00, 25),  # Тук ще се приложи 5% отстъпка
    Market(1003, "Downshifter 12", "Nike", 25.00, 15), # Тук ще се приложи 7% отстъпка
    Market(1004, "Jordan Low", "Nike", 210.00, 5),
    Market(1005, "Court Vision", "Nike", 35.00, 20)    # Тук ще се приложи 5% отстъпка
]
count = 0
for i in nike_products:
    if i.manufacturer == "Nike":
        count += i.price

count = count / len(nike_products)



# def search_by_manufacturer(product_list , manufacturer):
#     for product in product_list:
#         if product.manufacturer == manufacturer and product.price <= count:
#             print(product.name , product.price)
#
# search_by_manufacturer(nike_products, "Nike")

# def sort_by_quantity(nike_products):
#     sorted_nike_products = sorted(nike_products, key = lambda x: x.quantity) #mnogo vajno!!
#     for i in sorted_nike_products:
#         print(i.quantity , i.barcod , i.name, i.manufacturer, i.price)
#
# sort_by_quantity(nike_products)

def delete_by_name(product_list, name):
    product_list[:] = [p for p in product_list if not (p.name == name and p.quantity <= 3)]

    for i in product_list:
        print(f"Баркод: {i.barcod}, Име: {i.name}, Количество: {i.quantity}")


delete_by_name(nike_products, "Air Max 270")