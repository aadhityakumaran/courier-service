import mysql.connector

while True:
    install = input("Do you wish to setup Python Couriers? (Y/N): ")
    if install.upper() == "Y":
        break
    elif install.upper() == "N":
        exit()
    else:
        print("Invalid input")

password = input("Enter mysql password: ")

db = mysql.connector.connect(host="localhost", user="root", password=password)
cr = db.cursor()

# creating database
cr.execute("CREATE DATABASE py_couriers")
cr.execute("USE py_couriers")

# creating users table
cr.execute("""CREATE TABLE users (
username varchar(50) PRIMARY KEY,
password char(64)
)""")

# creating courier charge table
cr.execute("""CREATE TABLE charge (
weight_in_kg int,
cost_in_rupees int
)""")

cr.execute("""INSERT INTO charge VALUES
(1, 50),
(2, 75),
(3, 100),
(4, 125),
(5, 150),
(10, 275),
(20, 525),
(30, 775),
(40, 1025),
(50, 1275),
(100, 2520),
(150, 3770),
(200, 5020),
(250, 6270),
(300, 7520),
(350, 8770),
(400, 10020),
(450, 11270),
(500, 12520)
""")

# creating delivery people table
cr.execute("""CREATE TABLE deliverers (
deliverer_id int PRIMARY KEY,
city varchar(10),
deliverer_name varchar(99),
deliverer_phone_number char(10)
)""")

cr.execute("""INSERT INTO deliverers VALUES
(101, "Chennai", "Rajesh", "3254687325"),
(102, "Chennai", "Kumar", "3765498204"),
(103, "Chennai", "Saravanan", "3549071274"),
(104, "Chennai", "Pandian", "3649712540"),
(201, "Cochin", "Santhosh", "3799412987"),
(202, "Cochin", "Manoj", "3876299875"),
(203, "Cochin", "Akhil", "3762373295"),
(204, "Cochin", "George", "3431209883"),
(301, "Bangalore", "Ravi", "3987520432"),
(302, "Bangalore", "Girish", "3742992730"),
(303, "Bangalore", "Sridhar", "3357320939"),
(304, "Bangalore", "Sunil", "3234003025"),
(401, "Hyderabad", "Venkatesh", "3898023539"),
(402, "Hyderabad", "Nagaraj", "3793298730"),
(403, "Hyderabad", "Srinivas", "3971221947"),
(404, "Hyderabad", "Haider", "3879507202")
""")

# creating couriers table
cr.execute("""CREATE TABLE couriers (
order_no int PRIMARY KEY AUTO_INCREMENT,
username varchar(99),
r_name varchar(99),
r_number char(10),
r_address varchar(200),
city varchar(20),
deliverer_id int, 
FOREIGN KEY (deliverer_id) REFERENCES deliverers(deliverer_id)
)""")
cr.execute("ALTER TABLE couriers AUTO_INCREMENT = 1001")

db.commit()
db.close()

print("Python Couriers is ready to use")

print("""
Press 1 to open py_couriers
Press 2 to uninstall py_couriers setup
Press enter to exit""")
start = input(">>> ")
print("===============================================================")
print()
if start == "1":
    import couriers
elif start == "2":
    import uninstall
