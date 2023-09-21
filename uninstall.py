import mysql.connector
import os

x = input("""Are you sure you want to uninstall py_couriers (Y/N)?
(All data including databases and downloaded forms will be permanently deleted)
>>> """)

while True:
    if x.upper() == "N":
        exit()
    elif x.upper() == "Y":
        break
    else:
        print("Invalid input, Enter Y if you wish to uninstall or N to exit uninstall.py")

sql_password = input("Enter mysql password: ")
db = mysql.connector.connect(host="localhost", user="root", password=sql_password, database="py_couriers")
cr = db.cursor()

# Deleting all created order forms
cr.execute("SELECT order_no, username FROM couriers")
for num, name in cr:
    filename = f"Order{num}@{name}.txt"
    if os.path.exists(filename):
        os.remove(filename)

cr.execute("DROP DATABASE py_couriers")
db.close()

print("Database cleared")
input()
