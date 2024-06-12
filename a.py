class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_gross_salary(self, basic_salary):
        da_pay = basic_salary * 0.95
        hra = basic_salary * 0.20
        gross_salary = basic_salary + da_pay + hra
        return gross_salary

    def calculate_net_salary(self, basic_salary):
        tax = basic_salary * 0.25
        epf = 3000
        net_salary = self.calculate_gross_salary(basic_salary) - tax - epf
        return net_salary

    def calculate_tax(self, basic_salary):
        return basic_salary * 0.25

    def print_pay_details(self, basic_salary):
        gross_salary = self.calculate_gross_salary(basic_salary)
        net_salary = self.calculate_net_salary(basic_salary)
        tax = self.calculate_tax(basic_salary)

        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: {basic_salary}")
        print(f"Gross Salary: {gross_salary}")
        print(f"Net Salary: {net_salary}")
        print(f"TAX: {tax}")

class Manager(Employee):
    def calculate_gross_salary(self, basic_salary):
        da_pay = basic_salary * 0.95
        hra = basic_salary * 0.20
        gross_salary = basic_salary + da_pay + hra
        return gross_salary

class Engineer(Employee):
    def calculate_gross_salary(self, basic_salary):
        da_pay = basic_salary * 0.80
        hra = basic_salary * 0.15
        gross_salary = basic_salary + da_pay + hra
        return gross_salary

manager = Manager(name="John")
engineer = Engineer(name="Alice")

basic_salary_manager = 30000
basic_salary_engineer = 20000

manager.print_pay_details(basic_salary_manager)
print("\n")
engineer.print_pay_details(basic_salary_engineer)
