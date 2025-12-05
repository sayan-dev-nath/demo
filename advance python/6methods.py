class Mobile:
    flag = True  # class variable

    def __init__(self):  # constructor
        self.model = "realme C17"  # instance variable

    def showModel(self):  # instance method
        price = 1000  # local variable
        print("realme C17")

    def getValue(self):  # accessor/getter method
        return self.model

    def setValue(self):  # mutator/setter method
        self.model = "realme Pro"

    @classmethod
    def check(cls):  # class method
        print(cls.flag)

    @staticmethod
    def add(a, b):  # static method
        print(a + b)


realme = Mobile()
realme.showModel()

print(realme.getValue())

realme.setValue()
print(realme.model)

Mobile.check()

Mobile.add(1, 2)
