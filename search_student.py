from students import students

def search_student():
    student_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")