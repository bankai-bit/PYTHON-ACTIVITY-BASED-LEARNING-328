n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks1 = float(input("Enter first exam marks: "))
    marks2 = float(input("Enter second exam marks: "))

    change = marks2 - marks1

    print("Student:", name)
    print("Improvement:", change)

    if change > 0:
        print("Performance improved")
    elif change < 0:
        print("Performance declined")
    else:
        print("No change")

    if marks2 < 35:
        print("Needs improvement")
    else:
        print("Pass")