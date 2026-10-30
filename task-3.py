n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total += amount

    print(name, "Amount:", amount)

if total >= 5000:
    discount = total * 0.15
elif total >= 2000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)