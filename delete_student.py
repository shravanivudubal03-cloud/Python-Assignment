from students import students

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")