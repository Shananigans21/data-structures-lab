# student_data.py
# This module initializes and manages student records.

# Define a list of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def display_students(student_list):
    """Function to display the list of students."""
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}, Major: {student[2]}") 

def filter_students_by_major(student_list, major):
    """Returns and displays students by major."""
    filtered = [student for student in student_list if student[2] == major]
    if filtered:
        print(f"\nStudents majoring in {major}:")
        display_students(filtered)
    else:
        print(f"\nNo students found in {major}.")

def student_generator(student_list, major):
    """Yields students by major (generator)."""
    return (student for student in student_list if student[2] == major)

def display_student_details(student_db):
    """Displays student details from dictionary."""
    print("\nStudent Details:")
    for sid, data in student_db.items():
        print(f"ID: {sid}, Name: {data['name']}, Major: {data['major']}, Courses: {data['courses']}")

def add_course(student_db, student_id, new_course):
    """Adds a course to a student's record."""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\n{new_course} added to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")

# Dictionary storing student data
student_dict = {
    101: {"name": "Alice Johnson", "major": "Computer Science", "courses": {"CS101", "CS102"}},
    102: {"name": "Bob Smith", "major": "Mathematics", "courses": {"MATH101", "MATH102"}},
    103: {"name": "Charlie Davis", "major": "Physics", "courses": {"PHYS101", "PHYS102"}},
}

if __name__ == "__main__":
    # Display all students
    display_students(students)

    # Filter students by major
    filter_students_by_major(students, "Computer Science")

    # Use generator to retrieve students lazily
    print("\nMathematics students (using generator):")
    math_gen = student_generator(students, "Mathematics")
    print(next(math_gen))
    print(next(math_gen))

    # Display detailed dictionary-based data
    display_student_details(student_dict)

    # Add a new course and display updated data
    add_course(student_dict, 101, "CS201")
    display_student_details(student_dict)
