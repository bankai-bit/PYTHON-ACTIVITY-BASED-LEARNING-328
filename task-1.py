consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

total = consultation + diagnostic + treatment

if total >= 5000:
    discount = total * 0.10
elif total >= 3000:
    discount = total * 0.05
else:
    discount = 0

bill = total - discount

print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", bill)

if bill >= 5000:
    print("High Payment Category")
else:
    print("Normal Payment Category")