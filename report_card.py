# Milestone 1: Basic Student Report Card App

students = []

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    avg = sum(marks) / len(marks)
    student = {'name': name, 'marks': marks, 'avg': avg}
    students.append(student)

def show_students():
    for s in students:
        print(f"{s['name']} - Marks: {s['marks']} - Avg: {s['avg']:.2f}")

while True:
    print("\n1. Add Student\n2. Show All\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        break
