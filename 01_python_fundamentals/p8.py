# while True:
#     num = int(input("Enter a number between 1 and 5: "))
#     print(f"You have entered {num}")
#     if num == 5:
#         print("You won!")
#         break

# i=0
# flag = False
# while i<3:
#     num = int(input("Enter a number between 1 and 5: "))
#     print(f"You have entered {num}")
#     if num == 5:
#         flag = True
#         break
#     i=i+1
# if flag==True:
#     print("You Won")
# else:
#     print("Better Luck Next Time")


i=0
while i<3:
    num = int(input("Enter a number between 1 and 5: "))
    print(f"You have entered {num}")
    if num == 5:
        print("You Won!")
        break
    i=i+1
else:
    print("Better Luck Next Time!")
