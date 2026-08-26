class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")
    student = Student(name, age, branch)
    with open("students.txt", "a") as file:
        file.write(name + "," + age + "," + branch + "\n")
    print("Student added successfully!")
def view_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                print("Name   :", data[0])
                print("Age    :", data[1])
                print("Branch :", data[2])
                print("-------------------")
    except FileNotFoundError:
        print("No students found.")
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice")