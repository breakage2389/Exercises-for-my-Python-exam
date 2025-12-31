import random
#10<= n <=50
#list1 n  duljina
#indx cheten -2500 -1300
#indx necheten 1111 4444

while True:
    try:
        n = int(input("Enter a number: "))
        if not (10 <= n <= 50):
            print("Invalid input")
            continue
        break
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)

list1 =[]
for i in range(n):
    while True:
        try:
            num = int(input("Enter a number: "))
            if i%2 == 0 and -2500 <= num<= -1300:
                list1.append(num)
                break
            if i % 2 == 1 and 1111 <= num <= 4444:
                list1.append(num)
                break
        except Exception as e:
            print(e)
list1_even = [x for x in list1 if 10 <= x <=99 and x %2 ==0]
print(sum(list1_even)/len(list1_even))

list2 = [x for x in list1 if 100 <= x <= 999 and x%3 ==0]

list2 = [13 if i% 2==1 else list2[i] for i in range(len(list2))]
