from students import students

def update_student():
    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student["id"] == student_id:

            print("\nStudent Found!")
            
            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("Student updated successfully!")
            return

    print("Student ID not found!")