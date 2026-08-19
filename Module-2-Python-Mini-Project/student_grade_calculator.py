# Codomax AI & ML Internship
# Module 2 - Python Mini Project
# Student Grade Calculator


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    return total, average, grade


print("====================================")
print("       STUDENT GRADE CALCULATOR")
print("====================================")

student_name = input("Enter student name: ")

subjects = [
    "Python",
    "Mathematics",
    "Data Science",
    "Artificial Intelligence",
    "Machine Learning"
]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


total, average, grade = calculate_result(marks)


print("\n====================================")
print("             RESULT")
print("====================================")

print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)

print("====================================")
print("Thank you for using the Student Grade Calculator!")
