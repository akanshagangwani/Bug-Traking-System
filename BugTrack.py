# Project:Bug Tracking System
#  ------------------------------------------
#  Total No. of Entities: 3
#  1) Employee (Types: Admin or Expert )
#  2) Customer
#  3) Bug
#  ------------------------------------------

#  Total No. of Modules: 4
#  ------------------------------------------
#  A) Login & Signup Module
#  B) Admin Module
#  C) Customer Module
#  D) Expert Module
#  ------------------------------------------

#  Functionalities of the module:-
#  =============================
#  A) Login Module
#  B) Admin Module

# Customer Services -  Manage  Services ( View, Search )
#   1.Customer: View All
#   2.Customer: Search - by Customer Name
#   3.Customer: Search - by Customer Login Id

# Employee Services -  Manage Employee (Admin & Expert types)(Add, View, Search, Edit, Activate/Deactivate)
#   4.Employee: Add New (Admin or Expert)
#   5.Employee: View All
#   6.Employee: Search - by Employee Name
#   7.Employee: Search - by Employee Login Id
#   8.Employee: Search - by Employee Type
#   9.Employee: Activate or Deactivate
#   10.Employee: Change Password

# Bug Services -  Manage Bug( View, Search, AssignBugToExpert )
#   11.Bug: View All
#   12.Bug: Search by bugId
#   13.Bug: Search by status
#   14.Bug: Search by custLoginId
#   15.Bug: Assign to Expert
#   16.Logout

# C)Customer Module
#       1) Create Account
#       2) Update Account
#       3) Post New Bug
#       4) View All Bugs
#       5) Search Bugs based on status
#       6) View Bug Solution
#       7) Change Password

# D) Expert Module
#       1) View Assigned Bug
#       2) Filter Assigned Bugs based on status
#       3) Solve the Bug
#       4) Change Password



# =======================================
# SQL Scripts for creating Tables of the Project
# =======================================

# Table-01: employee (To store ADMIN or EXPERT type of employees)
# ------------------------------------
# create table employee
# (
# empLoginId varchar(10) primary key,
# empPassword varchar(20),
# empType varchar(20) ,
# empName varchar(45),
# empPhone varchar(10),
# empEmail varchar(45),
# empStatus varchar(20) DEFAULT 'ACTIVE'
# );

# insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail )
# values('AD1001', 'password', 'ADMIN', 'Akansha Gangwani', '9998887776', 'help@admin.com');

# insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail )
# values('EX3001', 'password', 'EXPERT', 'Karan', '4444444', 'expert@admin.com');


# Table-02: customer
# ------------------------------------
# create table customer
# (
# custLoginId varchar(10) primary key,
# custPassword varchar(20),
# custName varchar(45),
# custAge int,
# custPhone varchar(10),
# custEmail varchar(45)
# );

# insert into customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail )
# values('CU2001', 'password', 'Khushi', 21, '9998887776', 'priya@demo.com');

# insert into customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail )
# values('CU2002', 'password', 'Aryan', 22, '9998887776', 'priya@demo.com');

# Table-03: bug
# ------------------------------------
# create table Bug
# ( bugId int primary key auto_increment,
# bugPostingDate datetime default now(),
# custLoginId varchar(10) NOT NULL,
# bugStatus varchar(20) default 'New Bug',
# productName varchar(45) NOT NULL,
# bugDesc text NOT NULL,
# expertAssignedDate datetime default NULL,
# expertLoginId varchar(10) default NULL,
# bugSolvedDate datetime default NULL,
# solution text default NULL
# );



# insert into Bug(custLoginId, productName, bugDesc)
# values('CU2001', 'Laptop', 'Screen is flickring');

# insert into Bug(custLoginId, productName, bugDesc)
# values('CU2001', 'Mobile', 'Keyboard not working.');

# insert into Bug(custLoginId, productName, bugDesc)
# values('CU2002', 'Laptop', 'Wifi connection issues');


# For Example:-
# Following updation will be done by admin type of employee
# update bug set expertLoginId='EX3001',bugStatus='Assigned',expertAssignedDate=now() where bugid=2 ;


# Following updation will be done by expert type of employee
# update bug set bugSolvedDate=now(), bugStatus='Solved', solution='Pls visit nearest service center' where bugid=2 ;

import mysql.connector

# Establishing connection with MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="bugtrack_db"
)

# Function to display menu and get user choice
def display_menu():
    print("Bug Tracking System")
    print("-------------------")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice

# Function to handle login functionality
def login():
    LoginId = input("Enter your LoginId: ")
    password = input("Enter your password: ")

    # Check if the user is an employee or customer
    if LoginId.startswith("AD"):
        employee_login(LoginId, password, "ADMIN")
    elif LoginId.startswith("EX"):
        employee_login(LoginId, password, "EXPERT")
    elif LoginId.startswith("CU"):
        customer_login(LoginId, password)
    else:
        print("Invalid LoginId")

# Function to handle employee login
def employee_login(LoginId, password, emp_type):
    # Check if the employee exists in the database
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE empLoginId = %s AND empPassword = %s AND empType = %s", (LoginId, password, emp_type))
    employee = cursor.fetchone()

    if employee:
        print(f"Welcome, {employee[3]}!")
        if emp_type == "ADMIN":
            admin_module()
        elif emp_type == "EXPERT":
            expert_module()
    else:
        print("Invalid LoginId or password")

# Function to handle customer login
def customer_login(LoginId, password):
    # Check if the customer exists in the database
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customer WHERE custLoginId = %s AND custPassword = %s", (LoginId, password))
    customer = cursor.fetchone()

    if customer:
        print("Welcome, {customer[2]}!")
        customer_module()
    else:
        print("Invalid LoginId or password")

# Function to handle signup functionality
def signup():
    LoginId = input("Enter a LoginId: ")
    password = input("Enter a password: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")

    if LoginId.startswith("CU"):
        # Add the customer to the database
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO customer (custLoginId, custPassword, custName, custAge, custPhone, custEmail) VALUES (%s, %s, %s, %s, %s, %s)", (LoginId, password, name, age, phone, email))
        mydb.commit()
        print("Customer created successfully!")
    else:
        print("Invalid username")

# Function to handle the admin module
def admin_module():
    while True:
        print("\nAdmin Module")
        print("1. Manage Customer Services")
        print("2. Manage Employee Services")
        print("3. Manage Bug Services")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_customer_services()
        elif choice == "2":
            manage_employee_services()
        elif choice == "3":
            manage_bug_services()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# Function to handle the customer module
def customer_module():
    while True:
        print("\nCustomer Module")
        print("1. Create Account")
        print("2. Update Account")
        print("3. Post New Bug")
        print("4. View All Bugs")
        print("5. Search Bugs based on status")
        print("6. View Bug Solution")
        print("7. Change Password")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            update_account()
        elif choice == "3":
            post_bug()
        elif choice == "4":
            view_all_bugs()
        elif choice == "5":
            search_bugs_by_status()
        elif choice == "6":
            view_bug_solution()
        elif choice == "7":
            change_password("CU")
        elif choice == "8":
            break
        else:
            print("Invalid choice")

# Function to handle the expert module
def expert_module():
    while True:
        print("\nExpert Module")
        print("1. View Assigned Bug")
        print("2. Filter Assigned Bugs based on status")
        print("3. Solve the Bug")
        print("4. Change Password")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_assigned_bug()
        elif choice == "2":
            filter_assigned_bugs_by_status()
        elif choice == "3":
            solve_bug()
        elif choice == "4":
            change_password("EX")
        elif choice == "5":
            break
        else:
            print("Invalid choice")

# Function to handle managing customer services by the admin
def manage_customer_services():
    while True:
        print("\nCustomer Services")
        print("1. View All Customers")
        print("2. Search Customer by Name")
        print("3. Search Customer by Login ID")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_customers()
        elif choice == "2":
            search_customer_by_name()
        elif choice == "3":
            search_customer_by_login_id()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# Function to view all customers
def view_all_customers():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customer")
    customers = cursor.fetchall()

    if customers:
        print("Customers:")
        for customer in customers:
            print(f"Customer ID: {customer[0]}")
            print(f"Name: {customer[2]}")
            print(f"Age: {customer[3]}")
            print(f"Phone: {customer[4]}")
            print(f"Email: {customer[5]}")
            print()
    else:
        print("No customers found")

# Function to search for a customer by name
def search_customer_by_name():
    name = input("Enter the customer name: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customer WHERE custName LIKE %s", ('%' + name + '%',))
    customers = cursor.fetchall()

    if customers:
        print("Customers:")
        for customer in customers:
            print(f"Customer ID: {customer[0]}")
            print(f"Name: {customer[2]}")
            print(f"Age: {customer[3]}")
            print(f"Phone: {customer[4]}")
            print(f"Email: {customer[5]}")
            print()
    else:
        print("No customers found")

# Function to search for a customer by login ID
def search_customer_by_login_id():
    login_id = input("Enter the customer login ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customer WHERE custLoginId = %s", (login_id,))
    customer = cursor.fetchone()

    if customer:
        print("Customer Details:")
        print(f"Customer ID: {customer[0]}")
        print(f"Name: {customer[2]}")
        print(f"Age: {customer[3]}")
        print(f"Phone: {customer[4]}")
        print(f"Email: {customer[5]}")
    else:
        print("Customer not found")

# Function to handle managing employee services by the admin
def manage_employee_services():
    while True:
        print("\nEmployee Services")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employee by Name")
        print("4. Search Employee by Login ID")
        print("5. Search Employee by Type")
        print("6. Activate or Deactivate Employee")
        print("7. Change Employee Password")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee_by_name()
        elif choice == "4":
            search_employee_by_login_id()
        elif choice == "5":
            search_employee_by_type()
        elif choice == "6":
            activate_deactivate_employee()
        elif choice == "7":
            change_password("AD")
        elif choice == "8":
            break
        else:
            print("Invalid choice")

# Function to add a new employee
def add_new_employee():
    emp_type = input("Enter the employee type (ADMIN/EXPERT): ")
    emp_login_id = input("Enter the employee login ID: ")
    emp_password = input("Enter the employee password: ")
    emp_name = input("Enter the employee name: ")
    emp_phone = input("Enter the employee phone number: ")
    emp_email = input("Enter the employee email address: ")

    cursor = mydb.cursor()
    cursor.execute("INSERT INTO employee (empLoginId, empPassword, empType, empName, empPhone, empEmail) VALUES (%s, %s, %s, %s, %s, %s)", (emp_login_id, emp_password, emp_type, emp_name, emp_phone, emp_email))
    mydb.commit()
    print("Employee added successfully!")

# Function to view all employees
def view_all_employees():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()

    if employees:
        print("Employees:")
        for employee in employees:
            print(f"Employee ID: {employee[0]}")
            print(f"Name: {employee[3]}")
            print(f"Type: {employee[2]}")
            print(f"Phone: {employee[4]}")
            print(f"Email: {employee[5]}")
            print(f"Status: {employee[6]}")
            print()
    else:
        print("No employees found")

# Function to search for an employee by name
def search_employee_by_name():
    name = input("Enter the employee name: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE empName LIKE %s", ('%' + name + '%',))
    employees = cursor.fetchall()

    if employees:
        print("Employees:")
        for employee in employees:
            print(f"Employee ID: {employee[0]}")
            print(f"Name: {employee[3]}")
            print(f"Type: {employee[2]}")
            print(f"Phone: {employee[4]}")
            print(f"Email: {employee[5]}")
            print(f"Status: {employee[6]}")
            print()
    else:
        print("No employees found")

# Function to search for an employee by login ID
def search_employee_by_login_id():
    login_id = input("Enter the employee login ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE empLoginId = %s", (login_id,))
    employee = cursor.fetchone()

    if employee:
        print("Employee Details:")
        print(f"Employee ID: {employee[0]}")
        print(f"Name: {employee[3]}")
        print(f"Type: {employee[2]}")
        print(f"Phone: {employee[4]}")
        print(f"Email: {employee[5]}")
        print(f"Status: {employee[6]}")
    else:
        print("Employee not found")

# Function to search for an employee by type
def search_employee_by_type():
    emp_type = input("Enter the employee type (ADMIN/EXPERT): ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employee WHERE empType = %s", (emp_type,))
    employees = cursor.fetchall()

    if employees:
        print("Employees:")
        for employee in employees:
            print(f"Employee ID: {employee[0]}")
            print(f"Name: {employee[3]}")
            print(f"Type: {employee[2]}")
            print(f"Phone: {employee[4]}")
            print(f"Email: {employee[5]}")
            print(f"Status: {employee[6]}")
            print()
    else:
        print("No employees found")

# Function to activate or deactivate an employee
def activate_deactivate_employee():
    emp_login_id = input("Enter the employee login ID: ")
    emp_status = input("Enter the employee status (ACTIVE/INACTIVE): ")

    cursor = mydb.cursor()
    cursor.execute("UPDATE employee SET empStatus = %s WHERE empLoginId = %s", (emp_status, emp_login_id))
    mydb.commit()

    if cursor.rowcount > 0:
        print("Employee status updated successfully!")
    else:
        print("Employee not found")

# Function to handle managing bug services by the admin
def manage_bug_services():
    while True:
        print("\nBug Services")
        print("1. View All Bugs")
        print("2. Search Bug by ID")
        print("3. Search Bug by Status")
        print("4. Assign Bug to Expert")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_bugs()
        elif choice == "2":
            search_bug_by_id()
        elif choice == "3":
            search_bug_by_status()
        elif choice == "4":
            assign_bug_to_expert()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

# Function to view all bugs
def view_all_bugs():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug")
    bugs = cursor.fetchall()

    if bugs:
        print("Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Customer Login ID: {bug[2]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print()
    else:
        print("No bugs found")

# Function to search for a bug by ID
def search_bug_by_id():
    bug_id = input("Enter the bug ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE bugId = %s", (bug_id,))
    bug = cursor.fetchone()

    if bug:
        print("Bug Details:")
        print(f"Bug ID: {bug[0]}")
        print(f"Posting Date: {bug[1]}")
        print(f"Customer Login ID: {bug[2]}")
        print(f"Status: {bug[3]}")
        print(f"Product Name: {bug[4]}")
        print(f"Description: {bug[5]}")
        print(f"Expert Assigned Date: {bug[6]}")
        print(f"Expert Login ID: {bug[7]}")
        print(f"Bug Solved Date: {bug[8]}")
        print(f"Solution: {bug[9]}")
    else:
        print("Bug not found")

# Function to search for a bug by status
def search_bug_by_status():
    status = input("Enter the bug status: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE bugStatus = %s", (status,))
    bugs = cursor.fetchall()

    if bugs:
        print("Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Customer Login ID: {bug[2]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print(f"Expert Assigned Date: {bug[6]}")
            print(f"Expert Login ID: {bug[7]}")
            print(f"Bug Solved Date: {bug[8]}")
            print(f"Solution: {bug[9]}")
            print()
    else:
        print("No bugs found")

# Function to assign a bug to an expert
def assign_bug_to_expert():
    bug_id = input("Enter the bug ID: ")
    expert_login_id = input("Enter the expert login ID: ")

    cursor = mydb.cursor()
    cursor.execute("UPDATE bug SET expertLoginId = %s, bugStatus = 'Assigned', expertAssignedDate = NOW() WHERE bugId = %s", (expert_login_id, bug_id))
    mydb.commit()

    if cursor.rowcount > 0:
        print("Bug assigned successfully!")
    else:
        print("Bug not found")

# Function to handle updating customer account
def update_account():
    cust_login_id = input("Enter your login ID: ")
    name = input("Enter your new name: ")
    age = int(input("Enter your new age: "))
    phone = input("Enter your new phone number: ")
    email = input("Enter your new email address: ")

    cursor = mydb.cursor()
    cursor.execute("UPDATE customer SET custName = %s, custAge = %s, custPhone = %s, custEmail = %s WHERE custLoginId = %s", (name, age, phone, email, cust_login_id))
    mydb.commit()

    if cursor.rowcount > 0:
        print("Account updated successfully!")
    else:
        print("Customer not found")

# Function to post a new bug
def post_bug():
    cust_login_id = input("Enter your login ID: ")
    product_name = input("Enter the product name: ")
    bug_desc = input("Enter the bug description: ")

    cursor = mydb.cursor()
    cursor.execute("INSERT INTO bug (custLoginId, productName, bugDesc) VALUES (%s, %s, %s)", (cust_login_id, product_name, bug_desc))
    mydb.commit()
    print("Bug posted successfully!")

# Function to view all bugs for a customer
def view_all_bugs():
    cust_login_id = input("Enter your login ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE custLoginId = %s", (cust_login_id,))
    bugs = cursor.fetchall()

    if bugs:
        print("Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print(f"Expert Assigned Date: {bug[6]}")
            print(f"Expert Login ID: {bug[7]}")
            print(f"Bug Solved Date: {bug[8]}")
            print(f"Solution: {bug[9]}")
            print()
    else:
        print("No bugs found")

# Function to search bugs by status for a customer
def search_bugs_by_status():
    cust_login_id = input("Enter your login ID: ")
    status = input("Enter the bug status: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE custLoginId = %s AND bugStatus = %s", (cust_login_id, status))
    bugs = cursor.fetchall()

    if bugs:
        print("Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print(f"Expert Assigned Date: {bug[6]}")
            print(f"Expert Login ID: {bug[7]}")
            print(f"Bug Solved Date: {bug[8]}")
            print(f"Solution: {bug[9]}")
            print()
    else:
        print("No bugs found")

# Function to view the solution for a bug
def view_bug_solution():
    bug_id = input("Enter the bug ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT solution FROM bug WHERE bugId = %s", (bug_id,))
    solution = cursor.fetchone()

    if solution:
        print("Bug Solution:")
        print(solution[0])
    else:
        print("Bug not found or no solution provided")

# Function to change the password for a customer or expert
def change_password(prefix):
    login_id = input("Enter your login ID: ")
    new_password = input("Enter your new password: ")

    cursor = mydb.cursor()
    cursor.execute(f"UPDATE {prefix.lower()} SET {prefix.lower()}Password = %s WHERE {prefix.lower()}LoginId = %s", (new_password, login_id))
    mydb.commit()

    if cursor.rowcount > 0:
        print("Password changed successfully!")
    else:
        print(f"{prefix} not found")

# Function to view assigned bugs for an expert
def view_assigned_bug():
    expert_login_id = input("Enter your login ID: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE expertLoginId = '%s' " % (expert_login_id))
    bugs = cursor.fetchall()

    if bugs:
        print("Assigned Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print(f"Expert Assigned Date: {bug[6]}")
            print(f"Bug Solved Date: {bug[8]}")
            print(f"Solution: {bug[9]}")
            print()
    else:
        print("No assigned bugs found")

# Function to filter assigned bugs by status for an expert
def filter_assigned_bugs_by_status():
    expert_login_id = input("Enter your login ID: ")
    status = input("Enter the bug status: ")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bug WHERE expertLoginId = %s AND bugStatus = %s", (expert_login_id, status))
    bugs = cursor.fetchall()

    if bugs:
        print("Assigned Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}")
            print(f"Posting Date: {bug[1]}")
            print(f"Status: {bug[3]}")
            print(f"Product Name: {bug[4]}")
            print(f"Description: {bug[5]}")
            print(f"Expert Assigned Date: {bug[6]}")
            print(f"Bug Solved Date: {bug[8]}")
            print(f"Solution: {bug[9]}")
            print()
    else:
        print("No assigned bugs found")

# Function for an expert to solve a bug
def solve_bug():
    bug_id = input("Enter the bug ID: ")
    solution = input("Enter the bug solution: ")

    cursor = mydb.cursor()
    cursor.execute("UPDATE bug SET bugStatus = 'Solved', bugSolvedDate = NOW(), solution = %s WHERE bugId = %s", (solution, bug_id))
    mydb.commit()

    if cursor.rowcount > 0:
        print("Bug solved successfully!")
    else:
        print("Bug not found")

# Main program loop
while True:
    choice = display_menu()

    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        break
    else:
        print("Invalid choice")

# Close the MySQL connection
mydb.close()
