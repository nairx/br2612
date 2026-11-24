# def greet():
#     print("Greeting!")

# greet()

#Positional Argument
# def add(a,b):
#     print(a+b)

# add(4,5)

# def add(a,b=0):
#     print(a+b)

# add(4)

#keyword argument
# def add(a,b):
#     print(a+b)

# add(b=4,a=5)


# def add(c,a,b):
#     print(a+b+c)

# add(4,a=5,b=9)


# def add(a,b,c):
#     print(a+b+c)

# add(4,c=5,b=9)


# def add(a,b,c):
#     return a+b+c

# result = add(2,3,4)
# print(result)


# def add(*args):
#     print(args)
#     return sum(args)

# result = add(2,3,5,6,8,9,6,5,4)
# print(result)



# def add(**kwargs):
#     return sum(kwargs.values())

# result  = add(a=4,b=5,c=9)
# print(result)



# def add(*args,**kwargs):
#     return sum(args)+sum(kwargs.values())

# result  = add(6,8,3,4,a=4,b=5,c=9)
# print(result)