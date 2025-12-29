#ai-generated var 3
import random

# while True:
#     try:
#         m = int(input('15<m <40'))
#         if not (15<m<40):
#             print('Greshka')
#             continue
#         break
#     except ValueError:
#         print('greshno info')
#         continue
#     except Exception as e:
#         print(e)
# n = 5  #za po-lesno
# x= random.randint(-4000 , -2000)
# y = random.randint(2500 , 5500)
#
# print(f'spisuka se zapulwa s celi chisla s m na broi el s interval ot [{x}; {y}]')
# exam_list_1 = []
#
# for i in range(n):
#     while True:
#         try:
#             add = int(input(f'chislo koeto e v interwala [{x}; {y}]'))
#             if x <= add <= y:
#                 exam_list_1.append(add)
#             break
#         except ValueError:
#             print('chislo koeto e v interwala value error ')
#         except Exception as e :
#             print('chislo koeto e v interwala - Exception')
# print(exam_list_1)
#
# test_list = [x for x in exam_list_1 if ((x//10)%10)%2 ==0 and x>0]
# print(sum(test_list))
# test_list.clear()
#
# count = 0
# for x in exam_list_1:
#     if 100 <= abs(x) <=999 and (x % 5 ==0  or x% 0 == 0) :
#         test_list.append(x)
#         count += 1
# print(sum(test_list)/count)
#
# #creating exam_list_2
# exam_list_2 = [x for x in exam_list_1 if x<0 and x%4 ==0]
#
# odd_indx_list2 = exam_list_2[1::2] #[0,1,2,3,4,5] -> 1 ,3,5 i taka natatuk
# c0unt = 0
# for x in odd_indx_list2:
#     if x %2 ==0:
#         c0unt += 1
# print(c0unt)
#
# avr_e2 = sum(exam_list_2)/len(exam_list_2)
# exam_list_2 = [0 if x<avr_e2 else x for x in exam_list_2]
#
# if len(exam_list_2)> len(exam_list_1):
#     exam_list_2.pop(-2)
#     exam_list_2.pop(1)
# elif len(exam_list_1)> len(exam_list_2):
#     exam_list_1.pop(-2)
#     exam_list_1.pop(1)
# else:
#     print('duljinata e ednakwa')

class TechShop:
    def __init__(self, serial_number , model , category, price ,stock):
        self.serial_number = serial_number
        self.model = model
        self.category = category
        self.price = price
        self.stock = stock
        #avtomatichno prilagane
        self.apply_promo()

    def restock(self ,amount):
        self.stock += amount
        return self.stock

    def apply_promo(self):
        if self.price >2000:
            self.price -= self.price*0.12
        elif 1000<= self.price <=2000:
            self.price -= self.price*0.08
        else:
            return self.price

# while True:
#     try:
#         n = int(input('n na broi instacii'))
#         if not n>0:
#             print('greshko n mst be n>0 ')
#             continue
#         break
#     except ValueError:
#         print('value error')
#     except Exception as e :
#         print(e)
#
# inventory_list = []
#serial_number , model , category, price ,stock
# for i in range(n):
#     while True:
#         try:
#             print(f"Number {i+1} in inventory")
#             serial_number = int(input('serial number: '))
#             model = input('model: ')
#             category = input('category: ')
#             price = float(input('price: '))
#             stock = int(input('stock: '))
#             inventory_list.append(TechShop(serial_number , model , category , price, stock))
#             break
#         except ValueError:
#             print('value error')
#         except Exception as e :
#             print(e)

inventory_list = [
    TechShop(101, "iPhone 15", "Phone", 2100, 10),
    TechShop(102, "Samsung S23", "Phone", 1500, 5),
    TechShop(103, "Kindle", "E-reader", 250, 20),
    TechShop(104, "MacBook Air", "Laptop", 2400, 3),
    TechShop(105, "Asus Vivobook", "Laptop", 1200, 8)
]
sredno_price = sum(item.price for item in inventory_list)/len(inventory_list)

def search_by_serial(inventory_list , serial_number):
    for item in inventory_list:
        if item.serial_number == serial_number:
            print(f'{item.serial_number} , {item.model} , {item.category}, {item.price}, {item.stock}')
        else:
            print(f'Nqma takowa info')

def filter_by_category(inventory_list , category):
    for item in inventory_list:
        if item.category == category and item.price > sredno_price:
            print(f'{item.product_name} , {item.model} , {item.category}, {item.price}, {item.stock}')

def sort_inventory(inventory_list):
    inventory_list.sort(key=lambda inventory_list: inventory_list.price)

def clear_low_stock(inventory_list , category):
    inventory_list[:]= [item for item in inventory_list if item.category == category and item.price > sredno_price ]