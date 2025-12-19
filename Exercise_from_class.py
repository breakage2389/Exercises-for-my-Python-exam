while True:
    try:
        n = int(input("Enter a number: "))
        if not (15 < n < 35):
            print("Invalid input |15 < n <35|")
            continue
        else:
            break
    except ValueError:
        print("Invalid input")
    except ArithmeticError:
        print("Invalid input -> arithmetic error")

l1= []
for i in range(n):
    while True:
        try:
            addn =int(input("Enter a number |300< addn < 3000: "))
            if not 300 < addn < 30000:
                print("Invalid input |300 < addn < 30000|")
                continue
            else:
                l1.append(addn)
                break
        except ValueError:
            print("Invalid input -> ValueError")
count = 0
for z in l1:

    if ((z //10)%10) %4 ==0: #Tuk proverqwame dali deseticata na dadeno chislo se deli na 4 bez ostatuk
        count += 1
print(count)
