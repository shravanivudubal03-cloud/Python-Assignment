from students import students

def view_students():
    if not students:
        print("No students found!")
        return

    print("\n===== All Students =====")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("----------------------")