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
