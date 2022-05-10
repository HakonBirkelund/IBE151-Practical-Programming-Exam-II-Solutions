# Task 2 (direct citation):
# Write a function that gets a list of tuples representing
# the courses and returns the number of students in the school. 
# No student is enrolled in more than one course.
# My assumption for the task is that the data is clean,
# so the function does not need to check the names of students.

def count_students(students: list) -> int:
    """Given a list with course and student tuples, returns the number of students enrolled in the school.

    Args:
        students (list): The list of courses and students, in tuples. 

    Returns:
        int: Total number of students enrolled in the school.
    """
    student_count = 0                # Initialize accumulator at 0
    for course, student in students: # Iterate over tuples (course, student):
        for i in student:            # For each student in the tuple
            student_count += 1       # add 1 to the total.
    return student_count             # return accumulator