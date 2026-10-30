students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []
    print("Student", i + 1)

    for j in range(subjects):
        mark = float(input("Enter subject marks: "))
        row.append(mark)

    marks.append(row)

for i in range(students):
    total = sum(marks[i])
    average = total / subjects

    print("Student", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", average)

    if average >= 75:
        print("Grade: Distinction")
    elif average >= 60:
        print("Grade: First Class")
    elif average >= 35:
        print("Grade: Pass")
    else:
        print("Grade: Fail")

for j in range(subjects):
    total = 0

    for i in range(students):
        total += marks[i][j]

    print("Subject", j + 1, "Average:", total / students)