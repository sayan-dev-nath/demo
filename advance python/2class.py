"""
class ClassName(object):
    def __init__(self): #constructor; used to initialize variable value
        self.variableName = value
    def methodName(self):
        body of method

"""

# TODO: how to create class
# class Mobile:
#     def __init__(self):
#         self.model = "Realme X"

#     def showModel(self):
#         print("Model:", self.model)


# class Mobile:
#     def __init__(self, m):
#         self.model = m # attribute

#     def showModel(self, p):  # formal argument
#         price = p  # local variable
#         print("Model:", self.m, "Price:", price)


# TODO how to create object
# objectName = className(argument)
class Mobile(object):
    def __init__(self):
        self.model = "realme C17"

    def showModel(self, p):
        price = p
        print("Model:", self.model, "Price:", price)


ob = Mobile()
ob.showModel(10000)

ob.model = "realme pro"
ob.showModel(500000)
