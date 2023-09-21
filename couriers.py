import mysql.connector
import random
import login

db = mysql.connector.connect(host="localhost", user="root", password=login.sql_password, database="py_couriers")
cr = db.cursor()


def place_order():
    a = input("Enter the receiver's name: ")
    b = input("Enter the receiver's mobile number: ")
    c = input("Enter the receiver's address: ")

    # Choosing city from cities where deliverers are available
    cities_available = {}
    cr.execute("SELECT DISTINCT city FROM deliverers")
    for i, (city,) in enumerate(cr, start=1):
        cities_available[i] = city
    print("Choose receiver's city (or 0 to go back)")
    for key, city in cities_available.items():
        print(f"{key}: {city}")

    # Getting valid input
    while True:
        city_key = int(input(">>> "))
        if city_key == 0:
            return None     # Quits the function if num is 0
        if city_key in cities_available:
            city = cities_available[city_key]
            break
        else:
            print("Invalid input")
            print()

    # Selecting random deliverer from deliverers present
    cr.execute(f"SELECT deliverer_id FROM deliverers WHERE city = '{city}'")
    deliverers_available = []
    for (deliverer,) in cr:
        deliverers_available.append(deliverer)
    deliverer = deliverers_available[random.randrange(0, len(deliverers_available))]

    # Entering values into databases
    cr.execute(f"""INSERT INTO couriers (username, r_name, r_number, r_address, city, deliverer_id)
         VALUES ('{login.name}', '{a}', '{b}', '{c}', '{city}', {deliverer})""")
    db.commit()
    print("Order successfully placed")


def view_orders():
    cr.execute(f"SELECT order_no, r_name, r_number, city FROM couriers WHERE username = '{login.name}'")
    print(f"{'OrderNo'.ljust(10)}{'receiver'.ljust(20)}{'phone'.ljust(15)}city")
    for a, b, c, d in cr:
        print(f"{str(a).ljust(10)}{b.ljust(20)}{c.ljust(15)}{d}")


def view_rates():
    cr.execute(f"SELECT * FROM charge")
    print(f"{'Weight(kg)'.ljust(15)}cost(Rs)")
    for a, b in cr:
        print(f"{f'{a}kg'.ljust(15)}{f'{b}Rs'}")


def download_form():
    # Getting valid order number
    while True:
        order_no = int(input("Enter your order number (or 0 to go back): "))
        if order_no == 0:
            return None         # Quits the function if num is 0
        cr.execute(f"SELECT deliverer_id FROM couriers WHERE order_no = {order_no}")
        x = cr.fetchone()
        if x:
            del_id, = x
            break
        else:
            print("Order number does not exist, try again")
            print()

    # Sending deliverer info for order number to a file
    cr.execute(f"SELECT * FROM deliverers WHERE deliverer_id = {del_id}")
    a, b, name, city = cr.fetchone()
    filename = f"Order{order_no}@{login.name}.txt"

    with open(filename, 'w') as f:
        print(f"""Order Number: {order_no}\n
Your delivery person:
Name: {name}
Phone: {city}""", file=f)
    print(f"{filename} successfully downloaded")

    # viewing form
    while True:
        view = input("Do you wish to view your order form? (Y/N)")
        if view.upper() == "Y":
            with open(filename) as f:
                print(f.read())
            break
        elif view.upper() == "N":
            break
        else:
            print("Invalid input")


def view_form():
    while True:
        num = int(input("Enter your order number (or 0 to go back): "))
        if num == 0:
            return None         # Quits the function if num is 0
        filename = f"Order{num}@{login.name}.txt"

        # Tries to read file, if file not found prompts the order number again
        try:
            with open(filename) as f:
                print()
                print(f.read())
            break
        except FileNotFoundError:
            print(f"Order form not present in device for {num}")


while True:
    print("""Enter 1 to place a courier order
Enter 2 to check your pending courier orders
Enter 3 to see the courier charges
Enter 4 to download your courier order form
Enter 5 to view your courier order form
Enter 0 to quit""")
    choice = input(">>> ")
    print()

    if choice == "1":
        place_order()
        print("=======================================================")
        print()

    elif choice == "2":
        view_orders()
        print("=======================================================")
        print()

    elif choice == "3":
        view_rates()
        print("=======================================================")
        print()

    elif choice == "4":
        download_form()
        print("=======================================================")
        print()

    elif choice == "5":
        view_form()
        print("=======================================================")
        print()

    elif choice == "0":
        break

    else:
        print("Invalid Input. Try again")
        print()
