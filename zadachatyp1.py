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

lst_1 = [-25, 21 ,4,5 , 25 ,75, 50 ,125]
lst_2 = []
for num in lst_1:
    if 10<= num <= 99 or -99<= num <=-10:
        if num % 5 ==0:
            lst_2.append(num)
print(lst_2)


# collector = 1
# odd_lst_2 = lst_2[1::2]
# for i in odd_lst_2:
#     collector *= i
# print(collector)

lst_2 = [num for i, num in enumerate(lst_2) if not (i % 2 != 0 and num % 2 == 0)]
print(lst_2)

if len(lst_2) == len(lst_1):
    print('fine sa')
elif len(lst_2) < len(lst_1): #l2= [1,2,3,4]
    sreda = len(lst_2)//2
    novochislo = lst_2[0] * lst_2[-1]
    lst_2.insert(sreda, novochislo)
elif len(lst_1) > len(lst_2):
    sreda = len(lst_1) // 2
    novochislo = lst_1[0] * lst_1[-1]
    lst_1.insert(sreda, novochislo)