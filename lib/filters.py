# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """ Filter students by major using a list comprehension"""
    filtered = [student for student in student_list if student[2] == major]
    
    if filtered:
        print (f"\nStudents majoring in {major}:")
        for student in filtered:
            print(student)

    else: 
        print(f"\nNo students found in {major}.")
   
