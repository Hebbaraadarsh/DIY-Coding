
import sqlite3

#Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect('student_details.db')
cursor = conn.cursor()

# Create a table to store student information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        grade REAL
    )
''')

# Function to add a student to the database
def add_student(first_name, last_name, age, grade):
    cursor.execute('INSERT INTO students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)', (first_name, last_name, age, grade))
    conn.commit()
    print(f"Added student: {first_name} {last_name}")

# Function to retrieve all students from the database
def get_all_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for student in students:
        print(student)

# Function to search for a student by ID
def get_student_by_id(student_id):
    cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
    student = cursor.fetchone()
    if student:
        print(student)
    else:
        print("Student not found.")
# Function to update a student's information
def update_student(student_id, new_grade):
    cursor.execute('UPDATE students SET grade = ? WHERE student_id = ?', (new_grade, student_id))
    conn.commit()
    print(f"Updated grade for student ID {student_id}")

# Function to delete a student from the database
def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    print(f"Deleted student ID {student_id}")

# Main program loop
while True:
    print("\nStudent Information System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        add_student(first_name, last_name, age, grade)

    elif choice == '2':
        get_all_students()

    elif choice == '3':
        student_id = int(input("Enter student ID: "))
        get_student_by_id(student_id)

    elif choice == '4':
        student_id = int(input("Enter student ID: "))
        new_grade = float(input("Enter new grade: "))
        update_student(student_id, new_grade)

    elif choice == '5':
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)

    elif choice == '6':
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
