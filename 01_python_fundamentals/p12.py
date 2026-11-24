class InSufficientBalanceError(Exception):
    pass

balance = 5000
withdraw = int(input("Enter withdrawal amount: "))
try:
    if withdraw > balance:
        raise InSufficientBalanceError("Insufficient account balance")
    balance = balance - withdraw 
    print("Withdrawal successful")
    print("Available balance:",balance)
except InSufficientBalanceError as e:
    print(e)
