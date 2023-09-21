import mysql.connector
import hashlib

print("Welcome to Python Couriers")
input("Press enter to begin")

sql_password = input("Enter mysql password: ")
print()

db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="py_couriers")
cr = db.cursor()

while True:
    enter = input("""Enter 1 to LOGIN or 2 to CREATE NEW ACCOUNT (0 to exit): """)

    if enter == "0":
        exit()

    if enter == "1":        # GET NAME AND PASSWORD AND CHECK FROM users DATABASE
        attempt = 0
        while attempt < 5:
            name = input("Enter your username (Enter 0 to exit): ")
            if name == '0':
                exit()

            password = input("Enter your password: ")
            hashed = hashlib.sha256(password.encode()).hexdigest()

            cr.execute(f"SELECT * FROM users WHERE username = '{name}' and password = '{hashed}'")
            if cr.fetchone():
                break
            else:
                print("Incorrect password. Try again")
                attempt += 1
        else:
            print("Too many attempts")
            exit()
        break

    elif enter == "2":      # GETS NAME AND MAKES SURE ITS UNIQUE AND THEN GETS PASSWORD
        while True:
            name = input("Create a username (Enter 0 to exit): ")
            if name == '0':
                exit()
                
            cr.execute(f"SELECT username FROM users WHERE username = '{name}'")
            if cr.fetchone():
                print("Name already exists")
                
            else:
                while True:
                    password = input("Create your password: ")
                    if input("Confirm your password: ") == password:
                        break
                    else:
                        print("Passwords did not match. Try again")                        
                hashed = hashlib.sha256(password.encode()).hexdigest()
                
                cr.execute(f"INSERT INTO users VALUES ('{name}', '{hashed}')")
                db.commit()
                break
        break

    else:
        print("Invalid Input")
db.close()
print()
print("===============================================================")
print(f"HELLO {name}. WELCOME TO PYTHON COURIERS")
