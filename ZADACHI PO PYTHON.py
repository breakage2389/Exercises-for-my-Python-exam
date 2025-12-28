# Напишете програма, в която се създава списък с 12 на брой елементи.
# •	Всеки елемент задължително трябва да бъде цяло положително число, въведено от потребителя.
# •	Изведете броят на нечетните числа в списъка;
# •	Намерете средноаритметичната стойност на числата в списъка.


# l1  = []
# n = 0
# while n <12:
#     a = int(input('cqlo chislo molq'))
#     if a > 0:
#         l1.append(a)
#         n += 1
#     else:
#         print("Invalid num ,must be ->x >0")
#         continue
# print(l1)
# i=0
# for num in l1:
#     if num %2 !=0:
#         i+=1
#     else:
#         continue
# print(f'broqt na nechetnite chisla e {i}')
#
# sum =0
# for num in l1:
#     sum += num
# print(sum/len(l1))

# •	Създайте втори списък, който да съхранява петте най-големи числа от първия списък, които са кратни на 2;
# •	Сортирайте втория списък в низходящ ред;
# •	Да се изтрият всички елементи от втория списък, които са с четен индекс.
# l2=[]
# l1= [1,2,3,4,5,6,7,8,9,10,11,12]
# l1.sort(reverse=True) # 12 11 10 9 8 7 6 5 4
# for i in l1:
#     if i % 2 == 0:
#         l2.append(i)
#     if len(l2) == 5:
#         break
# print(l2)
# l2_final = l2[1::2]
# print(l2_final)

list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]

max_idx = None
max_el = None
for i,e in enumerate(list):
    if max_el is None or e > max_el:
        max_el = e
        max_idx = i

print(max_el,max_idx)
