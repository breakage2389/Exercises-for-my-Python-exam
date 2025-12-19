while True:
    try:
        number = int(input("15 < n < 35: "))
        if 15 < number < 35:
            break
        print("Number must be between 15 and 35")
    except ValueError:
        print("Enter a valid integer")

print(number)
