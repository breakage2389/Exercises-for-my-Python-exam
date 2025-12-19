# while True:
#     try:
#         n = int(input("Enter a number: "))
#         if not (15 < n < 35):
#             print("Invalid input |15 < n <35|")
#             continue
#         else:
#             break
#     except ValueError:
#         print("Invalid input")
#     except ArithmeticError:
#         print("Invalid input -> arithmetic error")
#
# l1= []
# for i in range(n):
#     while True:
#         try:
#             addn =int(input("Enter a number |300< addn < 3000: "))
#             if not 300 < addn < 30000:
#                 print("Invalid input |300 < addn < 30000|")
#                 continue
#             else:
#                 l1.append(addn)
#                 break
#         except ValueError:
#             print("Invalid input -> ValueError")
# count = 0
# for z in l1:
#
#     if ((z //10)%10) %4 ==0: #Tuk proverqwame dali deseticata na dadeno chislo se deli na 4 bez ostatuk
#         count += 1
# print(count)

#da se nameri  indexa na min element ot tozi spisuk koito ima statuk 4 pri celochisleno delenie na 6 ( x //6)
# numbers = [10, 25, 26, 28, 30, 27, 29]
# filtered = [x for x in numbers if x // 6 == 4]
# min_value = min(filtered)
# min_index = numbers.index(min_value)  # min_index = 1


#vtori spisuk
l1 = list(range(301, 317))
l2 =[]
ar = [] # for arthimethic l2
for i in l1:
    if i % 2 ==0 or i % 3 == 0:
        l2.append(i)
count_ar = 0
for idx, val in enumerate(l2):
    if val % 2 != 0:
        ar.append(val)
        count_ar += 1
print(ar)