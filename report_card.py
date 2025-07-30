# Milestone 1: Basic Student Report Card App

import os

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

# Milestone 2: Save/Load to File
def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{'|'.join(map(str, s['marks']))}\n")

def load_from_file():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                name, marks_str = line.strip().split(",")
                marks = list(map(int, marks_str.split("|")))
                avg = sum(marks) / len(marks)
                students.append({'name': name, 'marks': marks, 'avg': avg})

# Call this before starting
load_from_file()

def get_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    elif avg >= 60: return "C"
    else: return "D"

def show_students():
    for s in students:
        grade = get_grade(s['avg'])
        print(f"{s['name']} - Marks: {s['marks']} - Avg: {s['avg']:.2f} - Grade: {grade}")

while True:
    print("\n1. Add Student\n2. Show All\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        save_to_file()
    elif choice == '4':
        break
