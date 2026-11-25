class Example:
    def greet(self,name=None,age=None):
        if name and age:
            print("Hello ",name,age)
        elif name:
            print("Hello ",name)
        else:
            print("Hello")

example = Example()
example.greet()
example.greet("John")
example.greet("John",21)

