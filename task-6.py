balance = float(input("Enter initial balance: "))
transactions = int(input("Enter number of transactions: "))

for i in range(transactions):
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif choice == 1:
        balance += amount
        print("Deposit successful")
    elif choice == 2:
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    else:
        print("Invalid choice")

print("Final Balance:", balance)