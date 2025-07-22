class Student:
    def __init__(self,name,roll_no,m1,m2,m3):
        self.name=name
        self.roll_no=roll_no
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_total(self):
        self.total=self.m1+self.m2+self.m3
        print(f"total marks for {self.name} is {self.total}")

    def get_percentage(self):
        self.percentage=(self.total/(3*100))*100
        print(f"percentage of {self.name} is {self.percentage}%")

    def get_grade(self):
        if self.percentage>=90:
            print(f"grade is A+ for {self.name}")
        elif self.percentage>=75 and self.percentage<=89:
            print(f"grade is A for {self.name}")
        elif self.percentage>=55 and self.percentage<=74:
            print(f"grade is B for {self.name}")
        elif self.percentage>=40 and self.percentage<=54:
            print(f"grade is C for {self.name}")
        elif self.percentage>=35 and self.percentage<=39:
            print(f"{self.name} is passed")
        else:
            print(f"{self.name} is failed")

if __name__=="__main__":       
    s1=Student("Tejas Tanpure",234,77,88,90)
    s1.get_total()
    s1.get_percentage()
    s1.get_grade()

    s2=Student("Sonawane Om",230,99,91,95)
    s2.get_total()
    s2.get_percentage()
    s2.get_grade()

    s3=Student("Sarode Pranav",222,90,91,97)
    s3.get_total()
    s3.get_percentage()
    s3.get_grade()