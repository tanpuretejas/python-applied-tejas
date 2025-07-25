import json
def student_data(name,age,marks):
    student={"name":name,"age":age,"marks":marks}

    with open("student_data.json","w") as f:
        json.dump(student,f,indent=4)

def read_student_data():
    with open("student_data.json","r") as f:
        data=json.load(f)
        print("JSON data")
        print(f"name:{data["name"]},age:{data["age"]},marks:{data["marks"]}")
    
student_data("tejas",22,90)
read_student_data()

import csv
def saved_data(name,age,marks):
    with open("student1.csv","w",newline='') as f:
        writer=csv.writer(f)
        writer.writerow(["name","age","marks"])
        writer.writerow([name,age,marks])
def read_data():
    with open("student1.csv","r") as f:
        reader=csv.reader(f)
        print("CSV data")
        for row in reader:
            print(row)

saved_data("om",22,95)
read_data()