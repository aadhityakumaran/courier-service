# INTRODUCTION
In today's mobile-centric world, courier services have become indispensable. Consequently, the demand for efficient courier record management has surged. To address this need, we leverage Database Management Systems (DBMS) and programming languages such as Python to develop software capable of overseeing courier services from a centralized location, serving various parts of the globe.

Introducing *Python Couriers*, a compact yet powerful software project designed to seamlessly manage online courier services.

# USED MODULES
- sql_connector
- hashlib
- random
- os

# PROJECT DESIGN
Open the directory where the project is present.


### INSTALLING
We open setup.py that creates the database py_couriers which stores all the data. It contains 4 tables:
- users: Stores the account details of users
- charge: Stores the cost of sending couriers
- deliverers: Stores the details or delivery persons
- couriers: Stores the pending courier details
Now *Python Couriers* is ready to use.

**USING PYTHON COURIERS**
We open couriers.py and are taken to login.py for authentication by `import login`


**In login.py**:

We let the user create an account if he doesn’t have one and ask for a username and password. The password he gives is hashed using the `hashlib` module and stored in the *users* table along with the username. Since the password is not directly stored, no one can know the password except the user.

If the user does have an account, we let them log in. We hash the password he gives and if it matches with the hash in the *users* table. We let him try again. More than 5 attempts would cause the program to quit.

After authentication, the code returns to couriers.py



**In couriers.py:**

There are 6 options for the user to choose from
- Place an order:
The user enters the receiver’s details. He can choose the receiver’s city available cities where the courier service is available. His order is also assigned to a delivery person using the `random` module from deliverers available in the receiver’s city. This data along with a unique order number and username is stored in the *couriers* table.

- View orders:
The orders from the *couriers* table for the user’s username are displayed.

- Check courier charge:
Prints contents of *charge* table.

- Download order form:
Gets deliverer info from the order number. This info is written to a file named Order_ordnum_@_username_.txt

- View order form:
Prints out the contents of Order_ordnum_@_username_.txt

- Exit the program:
Calls exit()
