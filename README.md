# Student Record Management System

## 📌 Project Title

**Student Record Management System Using Python**

## 📖 Project Description

The **Student Record Management System** is a console-based Python application developed to manage student records in a simple and organized way.

The application allows users to **add, view, search, update, and delete** student records. The records are stored in a **JSON file**, so the data remains available even after the program is closed.

This project demonstrates the practical use of basic Python programming concepts in a single working application.

---

## 🎯 Project Objectives

* To develop a menu-driven console application.
* To manage student records using Python.
* To understand Python data types and data structures.
* To implement functions for different operations.
* To use conditional statements and loops.
* To handle invalid inputs using exception handling.
* To store and retrieve records using File I/O.
* To create a clean and organized Python project.

---

## ✨ Features

1. **Add Student Record**

   * Add student ID, name, age, course, and email.

2. **View Student Records**

   * Display all saved student records.

3. **Search Student Record**

   * Search for a student using their ID.

4. **Update Student Record**

   * Update existing student information.

5. **Delete Student Record**

   * Delete a student record after confirmation.

6. **File Storage**

   * Store records permanently in a JSON file.

7. **Exception Handling**

   * Handle invalid inputs and file-related errors.

8. **Menu-Driven Interface**

   * Easy-to-use console menu.

---

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* **File Handling**
* **GitHub**
* **VS Code / IDLE / PyCharm**

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Data Types
* Lists
* Dictionaries
* Conditional Statements
* `if`, `elif`, and `else`
* `for` Loop
* `while` Loop
* Functions
* Exception Handling
* File I/O
* JSON Data Storage

---

## 📂 Project Structure

```text
Student-Record-Management/
│
├── main.py
├── students.json
├── README.md
├── Assignment_Report.docx
│
└── screenshots/
    ├── main_menu.png
    ├── add_record.png
    ├── view_records.png
    ├── search_record.png
    ├── update_record.png
    └── delete_record.png
```

### File Description

| File/Folder              | Description                    |
| ------------------------ | ------------------------------ |
| `main.py`                | Main Python application        |
| `students.json`          | Stores student records         |
| `README.md`              | Project documentation          |
| `Assignment_Report.docx` | Complete project report        |
| `screenshots/`           | Screenshots of the application |

---

## 💻 Requirements

Python 3 or above is required.

Check your Python version:

```bash
python --version
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Record-Management.git
```

### Step 2: Open the Project Folder

```bash
cd Student-Record-Management
```

### Step 3: Run the Program

```bash
python main.py
```

---

## 📋 Application Menu

```text
========================================
 STUDENT RECORD MANAGEMENT SYSTEM
========================================
1. Add Student Record
2. View Student Records
3. Search Student Record
4. Update Student Record
5. Delete Student Record
6. Exit
========================================
Enter your choice (1-6):
```

---

## 📝 Sample Input and Output

### Add Student

```text
Enter your choice (1-6): 1

--- Add Student Record ---

Enter Student ID: 101
Enter Student Name: Shravani
Enter Student Age: 21
Enter Course: MCA
Enter Email: shravani@example.com

Student record added successfully.
```

### View Student

```text
Enter your choice (1-6): 2

--- Student Records ---

-----------------------------------
Student ID : 101
Name       : Shravani
Age        : 21
Course     : MCA
Email      : shravani@example.com
-----------------------------------
```

### Search Student

```text
Enter your choice (1-6): 3

Enter Student ID to search: 101

Student Found!

Student ID : 101
Name       : Shravani
Age        : 21
Course     : MCA
Email      : shravani@example.com
```

---

## 📄 Data Storage

Student records are stored in:

```text
students.json
```

Example:

```json
[
    {
        "id": 101,
        "name": "Shravani",
        "age": 21,
        "course": "MCA",
        "email": "shravani@example.com"
    }
]
```

The JSON file allows the application to save records permanently and load them when the program starts again.

---

## ⚠️ Exception Handling

The application handles common errors such as:

* Invalid student ID
* Invalid age
* Invalid menu choice
* Duplicate student ID
* Empty student information
* File reading errors
* Invalid JSON data

Example:

```text
Enter Student ID: abc

Invalid input. Please enter the correct data type.
```

---

## 🧪 Testing

| Test Case             | Expected Result                 |
| --------------------- | ------------------------------- |
| Add valid record      | Record added successfully       |
| Add duplicate ID      | Duplicate record rejected       |
| View records          | All records displayed           |
| Search existing ID    | Student details displayed       |
| Search unavailable ID | Record not found message        |
| Update record         | Student details updated         |
| Delete record         | Student record deleted          |
| Invalid input         | Error message displayed         |
| Exit                  | Application closes successfully |

---

## 📸 Screenshots

Add screenshots of your working application in the `screenshots` folder.

### Main Menu

```text
screenshots/main_menu.png
```

### Add Student Record

```text
screenshots/add_record.png
```

### View Student Records

```text
screenshots/view_records.png
```

### Search Student Record

```text
screenshots/search_record.png
```

### Update Student Record

```text
screenshots/update_record.png
```

### Delete Student Record

```text
screenshots/delete_record.png
```

---

## ✅ Advantages

* Simple and easy to use.
* Beginner-friendly Python project.
* Menu-driven interface.
* Permanent data storage.
* Uses reusable functions.
* Includes exception handling.
* Easy to modify and improve.

---

## ⚠️ Limitations

* Console-based application.
* Uses JSON instead of a database.
* No user authentication.
* Designed for basic student record management.
* Does not support multiple users simultaneously.

---

## 🚀 Future Enhancements

The project can be improved by adding:

* Student marks and grades.
* Attendance management.
* Login and authentication.
* Search by name or course.
* Sorting and filtering.
* CSV/Excel export.
* SQLite or MySQL database.
* Graphical User Interface using Tkinter.

---

## 📚 Learning Outcomes

Through this project, I learned how to:

* Create a Python console application.
* Use lists and dictionaries.
* Create and use functions.
* Implement loops and conditional statements.
* Handle errors using `try` and `except`.
* Read and write files.
* Store structured data using JSON.
* Create and manage a GitHub repository.

---

## 👩‍💻 Author

**Shravani Dubal**

**Course:** MCA

**Project:** Mini Project – Console Record-Management Application

**Academic Year:** 2026

---

## 📌 GitHub Repository

```text
https://github.com/YOUR-USERNAME/Student-Record-Management
```

Replace `YOUR-USERNAME` with your actual GitHub username.

---

## 📄 Assignment Documentation

The complete project report is available in:

```text
Assignment_Report.docx
```

---

## 📜 License

This project was created for educational and academic purposes.
