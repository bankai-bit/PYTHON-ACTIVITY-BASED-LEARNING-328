marks = []

for i in range(5):
    mark = int(input("Enter marks out of 100: "))
    marks.append(mark)

for i in range(5):
    if marks[i] < 35 and marks[i] >= 32:
        marks[i] += 3

print("Final Marks:", marks)

total = sum(marks)
average = total / 5

print("Total Marks:", total)
print("Average:", average)

if min(marks) >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")

if average >= 75 and min(marks) >= 35:
    print("Distinction")
elif average >= 60 and min(marks) >= 35:
    print("First Class")