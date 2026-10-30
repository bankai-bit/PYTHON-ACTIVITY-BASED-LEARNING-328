attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

percentage = attended / total * 100

print("Current Attendance:", percentage, "%")

required = 75
extra = 0

while (attended + extra) / (total + extra) * 100 < required:
    extra += 1

print("Additional classes required:", extra)