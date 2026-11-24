try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    result = a / b 
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Enter only numeric values")
except Exception as e:
    print("Something went wrong")
    print("Error Message",e)
else:
    print("Result",result)
finally:
    print("Program Completed")