class Employee:
    def __init__(self, name, login_id, employee_type):
        self.name = name
        self.login_id = login_id
        self.employee_type = employee_type
        self.active = True

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True


class Customer:
    def __init__(self, name, login_id):
        self.name = name
        self.login_id = login_id


class Bug:
    def __init__(self, bug_id, status, customer_login_id):
        self.bug_id = bug_id
        self.status = status
        self.customer_login_id = customer_login_id
        self.assigned_expert = None

    def assign_to_expert(self, expert):
        self.assigned_expert = expert


class BugTrackingSystem:
    def __init__(self):
        self.employees = []
        self.customers = []
        self.bugs = []
        self.current_user = None

    def login_module(self):
        login_id = input("Enter login ID: ")
        password = input("Enter password: ")
        # Perform login logic

    def admin_module(self):
        while True:
            print("1. Customer: View All")
            print("2. Customer: Search - by Customer Name")
            print("3. Customer: Search - by Customer Login ID")
            print("4. Employee: Add New (Admin or Expert)")
            print("5. Employee: View All")
            print("6. Employee: Search - by Employee Name")
            print("7. Employee: Search - by Employee Login ID")
            print("8. Employee: Search - by Employee Type")
            print("9. Employee: Activate or Deactivate")
            print("10. Employee: Change Password")
            print("11. Bug: View All")
            print("12. Bug: Search by bug ID")
            print("13. Bug: Search by status")
            print("14. Bug: Search by customer Login ID")
            print("15. Bug: Assign to Expert")
            print("16. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.view_all_customers()
            elif choice == 2:
                customer_name = input("Enter customer name: ")
                self.search_customer_by_name(customer_name)
            elif choice == 3:
                customer_login_id = input("Enter customer login ID: ")
                self.search_customer_by_login_id(customer_login_id)
            elif choice == 4:
                self.add_new_employee()
            elif choice == 5:
                self.view_all_employees()
            elif choice == 6:
                employee_name = input("Enter employee name: ")
                self.search_employee_by_name(employee_name)
            elif choice == 7:
                employee_login_id = input("Enter employee login ID: ")
                self.search_employee_by_login_id(employee_login_id)
            elif choice == 8:
                employee_type = input("Enter employee type: ")
                self.search_employee_by_type(employee_type)
            elif choice == 9:
                employee_login_id = input("Enter employee login ID: ")
                self.activate_deactivate_employee(employee_login_id)
            elif choice == 10:
                employee_login_id = input("Enter employee login ID: ")
                self.change_employee_password(employee_login_id)
            elif choice == 11:
                self.view_all_bugs()
            elif choice == 12:
                bug_id = input("Enter bug ID: ")
                self.search_bug_by_id(bug_id)
            elif choice == 13:
                bug_status = input("Enter bug status: ")
                self.search_bug_by_status(bug_status)
            elif choice == 14:
                customer_login_id = input("Enter customer login ID: ")
                self.search_bug_by_customer_login_id(customer_login_id)
            elif choice == 15:
                bug_id = input("Enter bug ID: ")
                expert_login_id = input("Enter expert login ID: ")
                self.assign_bug_to_expert(bug_id, expert_login_id)
            elif choice == 16:
                self.current_user = None
                break
            else:
                print("Invalid choice. Try again.")

    def customer_module(self):
        while True:
            print("1. Create Account")
            print("2. Update Account")
            print("3. Post New Bug")
            print("4. View All Bugs")
            print("5. Search Bugs based on status")
            print("6. View Bug Solution")
            print("7. Change Password")
            print("8. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_customer_account()
            elif choice == 2:
                customer_login_id = input("Enter customer login ID: ")
                self.update_customer_account(customer_login_id)
            elif choice == 3:
                customer_login_id = input("Enter customer login ID: ")
                self.post_new_bug(customer_login_id)
            elif choice == 4:
                self.view_all_bugs()
            elif choice == 5:
                bug_status = input("Enter bug status: ")
                self.search_bug_by_status(bug_status)
            elif choice == 6:
                bug_id = input("Enter bug ID: ")
                self.view_bug_solution(bug_id)
            elif choice == 7:
                customer_login_id = input("Enter customer login ID: ")
                self.change_customer_password(customer_login_id)
            elif choice == 8:
                self.current_user = None
                break
            else:
                print("Invalid choice. Try again.")

    def expert_module(self):
        while True:
            print("1. View Assigned Bug")
            print("2. Filter Assigned Bugs based on status")
            print("3. Solve the Bug")
            print("4. Change Password")
            print("5. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                expert_login_id = input("Enter expert login ID: ")
                self.view_assigned_bug(expert_login_id)
            elif choice == 2:
                expert_login_id = input("Enter expert login ID: ")
                bug_status = input("Enter bug status: ")
                self.filter_assigned_bugs(expert_login_id, bug_status)
            elif choice == 3:
                bug_id = input("Enter bug ID: ")
                self.solve_bug(bug_id)
            elif choice == 4:
                expert_login_id = input("Enter expert login ID: ")
                self.change_employee_password(expert_login_id)
            elif choice == 5:
                self.current_user = None
                break
            else:
                print("Invalid choice. Try again.")

    def view_all_customers(self):
        for customer in self.customers:
            print(f"Name: {customer.name}, Login ID: {customer.login_id}")

    def search_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name == name:
                print(f"Name: {customer.name}, Login ID: {customer.login_id}")
                return
        print("Customer not found.")

    def search_customer_by_login_id(self, login_id):
        for customer in self.customers:
            if customer.login_id == login_id:
                print(f"Name: {customer.name}, Login ID```python{customer.login_id}")
                return
        print("Customer not found.")

    def add_new_employee(self):
        name = input("Enter employee name: ")
        login_id = input("Enter employee login ID: ")
        employee_type = input("Enter employee type (Admin or Expert): ")
        employee = Employee(name, login_id, employee_type)
        self.employees.append(employee)
        print("Employee added successfully.")

    def view_all_employees(self):
        for employee in self.employees:
            print(
                f"Name: {employee.name}, Login ID: {employee.login_id}, Type: {employee.employee_type}, Active: {employee.active}")

    def search_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                print(
                    f"Name: {employee.name}, Login ID: {employee.login_id}, Type: {employee.employee_type}, Active: {employee.active}")
                return
        print("Employee not found.")

    def search_employee_by_login_id(self, login_id):
        for employee in self.employees:
            if employee.login_id == login_id:
                print(
                    f"Name: {employee.name}, Login ID: {employee.login_id}, Type: {employee.employee_type}, Active: {employee.active}")
                return
        print("Employee not found.")

    def search_employee_by_type(self, employee_type):
        for employee in self.employees:
            if employee.employee_type == employee_type:
                print(
                    f"Name: {employee.name}, Login ID: {employee.login_id}, Type: {employee.employee_type}, Active: {employee.active}")

    def activate_deactivate_employee(self, login_id):
        for employee in self.employees:
            if employee.login_id == login_id:
                if employee.active:
                    employee.deactivate()
                    print("Employee deactivated successfully.")
                else:
                    employee.activate()
                    print("Employee activated successfully.")
                return
        print("Employee not found.")

    def change_employee_password(self, login_id):
        for employee in self.employees:
            if employee.login_id == login_id:
                new_password = input("Enter new password: ")
                # Update employee password logic
                print("Password changed successfully.")
                return
        print("Employee not found.")

    def view_all_bugs(self):
        for bug in self.bugs:
            print(
                f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}, Assigned Expert: {bug.assigned_expert}")

    def search_bug_by_id(self, bug_id):
        for bug in self.bugs:
            if bug.bug_id == bug_id:
                print(
                    f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}, Assigned Expert: {bug.assigned_expert}")
                return
        print("Bug not found.")

    def search_bug_by_status(self, status):
        for bug in self.bugs:
            if bug.status == status:
                print(
                    f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}, Assigned Expert: {bug.assigned_expert}")

    def search_bug_by_customer_login_id(self, customer_login_id):
        for bug in self.bugs:
            if bug.customer_login_id == customer_login_id:
                print(
                    f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}, Assigned Expert: {bug.assigned_expert}")

    def assign_bug_to_expert(self, bug_id, expert_login_id):
        bug = None
        expert = None
        for b in self.bugs:
            if b.bug_id == bug_id:
                bug = b
                break
        for employee in self.employees:
            if employee.login_id == expert_login_id and employee.employee_type == "Expert":
                expert = employee
                break

        if bug and expert:
            bug.assign_to_expert(expert)
            print("Bug assigned to expert successfully.")
        elif not bug:
            print("Bug not found.")
        elif not expert:
            print("Expert not found.")

    def create_customer_account(self):
        name = input("Enter customer name: ")
        login_id = input("Enter customer login ID: ")
        customer = Customer(name, login_id)
        self.customers.append(customer)
        print("Customer account created successfully.")

    def update_customer_account(self, login_id):
        for customer in self.customers:
            if customer.login_id == login_id:
                new_name = input("Enter new name: ")
                customer.name = new_name
                print("Customer account updated successfully.")
                return
        print("Customer not found.")

    def post_new_bug(self, customer_login_id):
        for customer in self.customers:
            if customer.login_id == customer_login_id:
                bug_id = input("Enter bug ID: ")
                status = input("Enter bug status: ")
                bug = Bug(bug_id, status, customer_login_id)
                self.bugs.append(bug)
                print("Bug posted successfully.")
                return
        print("Customer not found.")

    def view_bug_solution(self, bug_id):
        for bug in self.bugs:
            if bug.bug_id == bug_id:
                # Retrieve and display bug solution logic
                print(f"Bug ID: {bug.bug_id}, Solution: <Bug Solution>")
                return
        print("Bug not found.")

    def change_customer_password(self, login_id):
        for customer in self.customers:
            if customer.login_id == login_id:
                new_password = input("Enter new password: ")
                # Update customer password logic
                print("Password changed successfully.")
                return
        print("Customer not found.")

    def view_assigned_bug(self, expert_login_id):
        for bug in self.bugs:
            if bug.assigned_expert and bug.assigned_expert.login_id == expert_login_id:
                print(f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}")

    def filter_assigned_bugs(self, expert_login_id, bug_status):
        for bug in self.bugs:
            if bug.assigned_expert and bug.assigned_expert.login_id == expert_login_id and bug.status == bug_status:
                print(f"Bug ID: {bug.bug_id}, Status: {bug.status}, Customer Login ID: {bug.customer_login_id}")

    def solve_bug(self, bug_id):
        for bug in self.bugs:
            if bug.bug_id == bug_id:
                # Solve bug logic
                print(f"Bug ID: {bug.bug_id} solved.")
                return
        print("Bug not found.")


def main():
    bug_tracking_system = BugTrackingSystem()

    while True:
        print("1. Login")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            bug_tracking_system.login_module()
            if bug_tracking_system.current_user:
                user_type = bug_tracking_system.current_user.employee_type
                if user_type == "Admin":
                    bug_tracking_system.admin_module()
                elif user_type == "Customer":
                    bug_tracking_system.customer_module()
                elif user_type == "Expert":
                    bug_tracking_system.expert_module()
            else:
                print("Login failed. Please try again.")
        elif choice == 2:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
