def student_data():
    name=input("enter student name:")
    while True:
        age=int(input(f"enter age of {name}:"))
        if age<0:
            print(f"Invalid age:{age}, age must be positive ")
        else:
            break
    while True:
        grade=input(f"enter grade of {name}:").upper()
        if grade not in ['A','B','C','D','E','F']:
            print(f"Invalid Grade:{grade}")
        else:
            break
    with open("student.txt","a") as f:
        f.write(f"{name},{age},{grade}\n")
    print("student data saved successfully...\n")

def display_student_data():
    try:
        with open("student.txt","r") as f:
            for line in f:
                name,age,grade=line.strip().split(",")
                print(f"name:{name} age:{age} grade:{grade}")
    except FileNotFoundError:
        print("no student data found\n")

def search_student_data():
    search_name=input("enter name of student to search:").strip().lower()
    try:
        with open("student.txt","r") as f:
            found=False
            for line in f:
                if not line.strip():
                    continue
                name,age,grade=line.strip().split(",")
                if name.strip().lower()==search_name:
                    print(f"student data found name:{name} age:{age} grade:{grade}")
                    found=True

            if not found:
                print(f"student data not found for {search_name}")
    except FileNotFoundError:
        print("student data not found!!!")

def main_menu():
    while True:
        choice=int(input("student data\n1 for save student data\n2 for display student data\n3 for searching student data\nenter here"))
        if choice==1:
            student_data()
        elif choice==2:
            display_student_data()
        elif choice==3:
            search_student_data()
        
        else:
            print("Invalid choice....please enter valid choice")

main_menu()