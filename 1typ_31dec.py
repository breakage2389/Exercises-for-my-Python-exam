import random

while True:
    try:
        n = int(input("Enter a number: "))
        if not(10<= n <=50):
            print("invalid number")
            continue
        break #mn vajen break koito go zabrawqm
    except ValueError:
        print("invalid number->value error")
    except Exception as e:
        print(e)
list1= []
a = random.randint(-2500,-1300)
b = random.randint(1111,4444)

for i in range(n):
    while True:
        try:
            number = int(input(f"Enter a number in range [{a}:{b}]: "))
            if a<=number<=b:
                list1.append(number)
                break
        except ValueError:
            print("invalid number->value error")
        except TypeError:
            print("invalid number->type error")
        except Exception as e:
            print(e)

list1_cus = [x for x in list1 if x < 0 and (((abs(x)//10)%10) %4 ==0 or ((abs(x)//10)%10) %5 ==0)]
count= len(list1_cus)

list1_even_cs = [x for x in list1 if 10<= x <=99 and x%2==0]
print(sum(list1_even_cs)/len(list1_even_cs))
# if list1_even_cs:
#     print(sum(list1_even_cs)/len(list1_even_cs))
# else:
#     print("No even two-digit numbers")

list2 =[x for x in list1 if 100<= x <=999 and x %3==0]

#broi
list2_custom = [x for x in list2 if x %2 !=0][0::2]
print(len(list2_custom))

list2 = [13 if i %2 == 0 else list2[i] for i in range(len(list2))]

