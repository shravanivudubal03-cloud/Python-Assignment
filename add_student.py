from students import students

def add_student():
    student_id = int(input("Enter Student ID: "))

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")