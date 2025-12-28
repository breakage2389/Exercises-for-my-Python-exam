#podobna zadacha na purwata
# cqlo chislo n  interwal 20 <= n <=40 try except
#list_a duljina n/ celi chisla ot user/ v interwal (p;q) p -> [-4000 ; -1500] q ->[2500 ;3500]
#list_a
#cifra na deseticite e nechetno type of list -ready
#index na el nai golqma stoinost where x % 5 == 2
#list_b -> 4 el ot list_a koito sa tricifreni i se x % 4 ==0

#list_b sum listb  where indx%2 ==0
# del nechetna stoinost i cheten indx

import random
# while True:
#     try:
#         n = int(input("Enter a number -> 20<=n<=40 "))
#         if 20 <= n <= 40:
#             break
#     except ValueError:
#         print("Invalid input")
#         continue
#     except Exception as e:
#         print(e)
#         continue
n= 5 # za po lesno
p = random.randint(-4000 , -1500)
q = random.randint(2500 , 3500)
print(p ,q)
list_a = []
for i in range(n):
        while True:
            try:
                num = int(input(f"Въведете число {i+1} в интервала ({p}; {q}): "))
                if p < num < q:
                    list_a.append(num)
                    break
                else:
                    print("Извън интервала, опитайте пак.")
            except ValueError:
                print("Невалиден вход.")

# l1st =[x for x in list_a if ((x//10)%10) %2 != 0]
# print(l1st)
max_el = None
max_idx = None

for i , e in enumerate(list_a):
    if e % 5 ==2:
        if max_el is None or e > max_el:
            max_el = e
            max_idx = i
print(max_idx)


# del nechetna stoinost i cheten indx
list_b = [x for x in list_a if 100<=x<=999 and x%4 ==0][:4]
print(list_b)

#print(sum(list_b[1::2]))

for x in list_b:
    if x in list_b[0::2] and x % 2 !=0:
        list_b.remove(x)
print(list_b)