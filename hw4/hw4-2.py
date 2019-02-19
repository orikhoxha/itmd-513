import os

'''
    This program reads a file and generates a report for each student GPA,
    credits sum, and the courses taken.
    
    Name: Orik Hoxha
    Class: ITMD 513
    
'''


# Fields to print on the generated report
FIELDS_TO_PRINT = "course_code,course_credits,course_grade"

# Header for each of the fields to be printed
FIELDS_HEADER = "Course Code, Course Credits, Course Grade"


'''
    fn: map_student_fields(field)
    Map the fields for a student row into numbers. Given a field  iex. "id" will return 0

    Parameters
    ----------
    arg1 : string
        field to be searched for

    Returns
    ---------
    int
        returns the position of a particular field in a Student row

'''

def map_student_fields(field):
    switcher = {
        "id": 0,
        "name": 1,
        "course_code": 2,
        "course_credits": 3,
        "course_grade": 4
    }
    return switcher.get(field, 0)


'''
    fn: student_equals(student_1, student_2)
    Compare two students whether they are equal based on their id's

    Parameters
    ----------
    arg1 : string
        user 1 to be compared
    
    arg2 : string
        user 2 to be compared

    Returns
    ---------
    Boolean
        returns True if the students are equal, else false.

'''


def student_equals(student_1, student_2):
    return get_student_field(student_1, "id") == get_student_field(student_2, "id")


'''
    fn: get_student_field(student, field)
    Splits the student row into fields, and gets a field at particular position

    Parameters
    ----------
    arg1 : string
        student row to extract the field from

    arg2 : string
        field to be extracted from the student

    Returns
    ---------
    string
        returns the String value of the particular field from the student.

'''


def get_student_field(student, field):
    return student.split()[map_student_fields(field)]


'''
    fn: calculate_semester_credits_per_student(student)
    Calculate the credits taken per semester for a particular student. Opens the file and iterates through
    each user, and checks whether they match with the student paramenter. If yes, calcuale the credits.

    Parameters
    ----------
    arg1 : string
        student to extract the credits from.

    Returns
    ---------
    string
        returns the sum of credits for a particular student.

'''


def calculate_semester_credits_per_student(student):
    students_file = open("students.txt", "r")
    student_credits = 0
    for s in students_file:
        if student_equals(s, student):
            student_credits += int(get_student_field(s, "course_credits"))

    students_file.close()
    return student_credits


'''
    fn: map_grade_letter_to_number(course_grade)
    Maps the course grade letter (A,B,C,D,F) to numbers respectively (4,3,2,1,0)

    Parameters
    ----------
    arg1 : string
        course grade as a letter.

    Returns
    ---------
    int
        returns the int representation of the grade.

'''


def map_grade_letter_to_number(course_grade):
    if course_grade == 'A':
        return 4
    elif course_grade == 'B':
        return 3
    elif course_grade == 'C':
        return 2
    elif course_grade == 'D':
        return 1
    else:
        return 0


'''
    fn: format_decimal_number(number, precision)
    Formats a decimal number according to the precision the user has entered.

    Parameters
    ----------
    arg1 : float
        number to be formatted
        
    arg2 : int
        decimal precision for the number iex. 2 - > 32.12

    Returns
    ---------
    float
        returns the number formatted.

'''


def format_decimal_number(number, precision):
    return round(number, precision)


'''
    fn: calculate_gpa_student(student, credits_sum)
    Calculates the gpa for a student. Opens the file, and compares all the rows against the student paramenter.
    If match, then it does the GPA calculation algorithm.

    Parameters
    ----------
    arg1 : string
        Student to calculate the GPA for.

    arg2 : int
        sum of the credits for a particular student.

    Returns
    ---------
    float
        returns the GPA for the student.

'''


def calculate_gpa_student(student, credits_sum):

    students_file = open("students.txt","r")

    course_grade_sum = 0
    for s in students_file:
        if student_equals(s, student):
            course_grade = get_student_field(s, "course_grade")
            course_grade_numerical = map_grade_letter_to_number(course_grade)
            course_grade_sum += (course_grade_numerical * int(get_student_field(s, "course_credits")))

    students_file.close()
    return format_decimal_number((course_grade_sum / credits_sum), 2)


'''
    fn: get_course_info_per_student(student)
    Gets all the courses taken by a particular student.

    Parameters
    ----------
    arg1 : string
        Student to get the courses for.

    Returns
    ---------
    string
        returns all the courses taken by a user in a specific format.

'''


def get_course_info_per_student(student):
    students_file = open("students.txt", "r")

    course_info = ""
    for s in students_file:
        if student_equals(student, s):
            for field in FIELDS_TO_PRINT.split(","):
                course_info += get_student_field(s, field) + '\t\t\t\t\t'
            course_info += '\n'

    students_file.close()

    return course_info


'''
    fn: generate_report_per_student(student, file_generate_report)
    Creates the header, retrieves the student information, and writes to a file for each student.

    Parameters
    ----------
    arg1 : string
        Student to output the information for.

    Returns
    ---------
    void

'''


def generate_report_per_student(student, file_generate_report):
    course_header = ""
    for header in FIELDS_HEADER.split(","):
        course_header += header + "\t\t"

    file_generate_report.write("Student Name: %s " % get_student_field(student, "name") + "\n")
    file_generate_report.write("Student ID Number: %s" % get_student_field(student, "id") + "\n")
    file_generate_report.write("\n")
    file_generate_report.write(course_header + "\n")
    file_generate_report.write('\u00af' * (len(course_header) + 3) + "\n")
    file_generate_report.write(get_course_info_per_student(student))
    file_generate_report.write("\n")

    credits_completed = calculate_semester_credits_per_student(student)

    file_generate_report.write("Total Semester Course Credits Completed: " + str(credits_completed) + "\n")
    file_generate_report.write("Semester GPA: " + str(calculate_gpa_student(student, credits_completed)))

    file_generate_report.write("\n\n\n\n")


'''
    fn: main()
    Opens the files to read/write  the student information from/to. Iterates for each student and generates the report.
    Closes the files at the end of the function.

'''


def main():

    if os.path.isfile("students.txt"):

        students_info = open("students.txt", "r")
        students_report = open("students_report.txt", "a+")

        previous_student_id = -1

        for student in students_info:

            if get_student_field(student, "id") == previous_student_id:
                continue
            else:
                previous_student_id = get_student_field(student, "id")
                generate_report_per_student(student, students_report)
        students_info.close()
        students_report.close()


if __name__ == '__main__':
    main()