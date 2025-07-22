class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display_details(self):
        print(f"name:{self.name}")
        print(f"ID:{self.emp_id}")
        print(f"salary:{self.salary}")

    def get_annual_salary(self):
        print(f"annual salary of {self.name} is:{self.salary*12}\n")

class Manager(Employee):
    def __init__(self,name,emp_id,salary,department):
        super().__init__(name,emp_id,salary)
        self.department=department
        
    def display_details(self):
        super().display_details()
        print(f"department:{self.department}")
    
    def get_annual_salary(self):
        print(f"annual salary of {self.name} is:{self.salary*12}\n")

class Developer(Employee):
    def __init__(self,name,emp_id,salary,language):
        super().__init__(name,emp_id,salary)
        self.language=language
    def display_details(self):
        super().display_details()
        print(f"language:{self.language}")

    def get_annual_salary(self):
        print(f"annual salary of {self.name} is:{self.salary*12}")

e1=Employee("Tejas Tanpure",234,1000000)
e1.display_details()
e1.get_annual_salary()
m1=Manager("Pranav Sarode",222,85000,"IT")
m1.display_details()
m1.get_annual_salary()
d1=Developer("Siddhesh Sonawane",232,90000,"Python")
d1.display_details()
d1.get_annual_salary()