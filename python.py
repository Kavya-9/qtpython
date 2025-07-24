student_fullname = input("enter your name:")
roll_number = input("enter your roll number:")
branch = input("enter yor branch:")
city = input("enter your city:")
section = input("enter your section:")
print("the student name is:", student_fullname)
print("the student roll number is:", roll_number)
print("student branch:", branch)
print("student city:", city)
print("student section:", section)

# subjects
python = input("enter 1st subject:")
java = input("enter 2nd subject:")
c = input("enter 3rd subject:")
print("the first subject is:", python)
print("the second subject is:", java)
print("the third subject is:", c)

# marks
python_marks = float(input("enter python marks:"))
java_marks = float(input("enter java marks:"))
c_marks = float(input("enter c marks:"))
print("python marks:", python_marks)
print("java_marks:", java_marks)
print("c_marks:", c_marks)

#  grades
pass_mark = 35.0
total_marks = python_marks + java_marks + c_marks
print("Total Marks:", total_marks)

if python_marks < pass_mark or java_marks < pass_mark or c_marks < pass_mark:
    print("Result: FAIL")
    grade = "F"
else:

    if total_marks >= 90:
        grade = "A"
    elif total_marks >= 80:
        grade = "B"
    elif total_marks >= 70:
        grade = "C"
    elif total_marks >= 60:
        grade = "D"
    else:
        grade = "E"
    print("Result: PASS")

print("Grade:", grade)









