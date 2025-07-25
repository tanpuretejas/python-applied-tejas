import json
import csv
def add_student_data():
    name=input("enter name of student:")
    age=input(f"enter age of {name}:")
    grade=input(f"enter grade of {name}:").upper()
    dict1={"name":name,"age":age,"grade":grade}

    with open("students.csv","a",newline='') as f:
        wr=csv.writer(f)
        wr.writerow(["name","age","grade"])
        wr.writerow([name,age,grade])

    with open("students.json","w") as f:
            json.dump(dict1,f,indent=4)

def read_json():
    with open("students.json","r") as f:
         data=json.load(f)
         print("JSON data")
         print(f"name:{data['name']},age:{data['age']},grade:{data['grade']}")

def read_csv():
     with open("students.csv","r") as f:
          read=csv.reader(f)
          print("CSV data")
          for row in read:
               print(row)

add_student_data()
read_json()
read_csv()