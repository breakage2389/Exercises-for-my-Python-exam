clothes_list = []

class ClothesShop:
    def __init__(self, id, brand, type, quantity):
        self.id = id
        self.brand = brand
        self.type = type
        self.quantity = quantity

    def info(self):
        return f'ID: {self.id}, Brand: {self.brand}, Type: {self.type}, Qty: {self.quantity}'


def search_by_id(clothes_list, id):
    for item in clothes_list:
        if item.id == id:
            print(item.info())
            return
    print("Не е открит такъв продукт")


def search_by_brand(clothes_list, brand):
    found = False
    for item in clothes_list:
        if item.brand == brand:
            print(item.info())
            found = True
    if not found:
        print("Няма артикули с тази марка")


def sell_clothes_by_id(clothes_list, id, num):
    for item in clothes_list:
        if item.id == id:
            if item.quantity >= num:
                item.quantity -= num
                print("Успешна продажба")
                print(f"Оставащо количество: {item.quantity}")
            else:
                print("Недостатъчна наличност")
            return
    print("Не е открит такъв продукт")



# =============================
#            MENU
# =============================

while True:
    print("\n============================")
    print("      CLOTHES SHOP MENU")
    print("============================")
    print("1. Add new item")
    print("2. Search by ID")
    print("3. Search by Brand")
    print("4. Sell Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\n--- Adding New Item ---")
        try:
            uid = int(input("Enter ID: "))
            ubrand = input("Enter Brand: ")
            utype = input("Enter Type: ")
            uqty = int(input("Enter Quantity: "))

            if uqty < 0:
                print("Error: Quantity cannot be negative!")
            else:
                new_item = ClothesShop(uid, ubrand, utype, uqty)
                clothes_list.append(new_item)
                print("Item added successfully!")
        except ValueError:
            print("ERROR: ID and Quantity must be numbers!")

    elif choice == '2':
        try:
            uid = int(input("Enter ID to search: "))
            search_by_id(clothes_list, uid)
        except ValueError:
            print("ERROR: ID must be a number.")

    elif choice == '3':
        ubrand = input("Enter Brand name: ")
        search_by_brand(clothes_list, ubrand)

    elif choice == '4':
        try:
            uid = int(input("Enter Item ID to sell: "))
            uqty = int(input("How many to sell?: "))

            if uqty <= 0:
                print("Error: You must sell at least 1 item.")
            else:
                sell_clothes_by_id(clothes_list, uid, uqty)

        except ValueError:
            print("ERROR: Numbers only please.")

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
