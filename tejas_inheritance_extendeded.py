class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Student(Person):
    def __init__(self,name,age,roll_no,branch):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.branch=branch

class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, branch,project_title):
        super().__init__(name, age, roll_no, branch)
        self._project_title=project_title

    @property
    def project_title(self):
        return f"project title:{self._project_title.upper()}"


    def display_details(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"roll_no:{self.roll_no}")
        print(f"branch:{self.branch}\n")
        
    
class Professor(Person):
    def __init__(self,name,age,employee_id,subject):
        super().__init__(name, age)
        self.employee_id=employee_id
        self.subject=subject
    def display_details(self):

        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"employee id:{self.employee_id}")
        print(f"subject:{self.subject}")

g=GraduateStudent("Tejas Tanpure",21,234,"computer","calculator")
print(g.project_title)
g.display_details()
p=Professor("Sonawane Om",20,230,"Python")
p.display_details()