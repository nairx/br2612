#Bank Management System
balance = 0
while True:
    print("\n ======= BANKING MANAGEMENT SYSTEM =======")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.View Balance")
    print("4.Exit")
    choice = input("Enter your choice:")
    match choice:
        case "1":
            deposit = float(input("Enter deposit amount:"))
            balance += deposit
            print("Amount Deposited Successfully")
            print(f"New balance: {balance}")
        case "2":
            print(f"Current balance: {balance}")
            withdraw = float(input("Enter withdraw amount:"))
            if withdraw > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw
                print("Amount Withdrawn Successfully")
                print(f"New balance: {balance}")
        case "3":
            print(f"Current balance: {balance}")
        case "4":
            print("Exit")
            break
        case _:
            print("Invalid choice")