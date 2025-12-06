# TODO: Single Inheritance
"""class Father:
    money = 1000

    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showMoney(cls):
        print("Parent Class Class Method:", cls.money)


class Son(Father):
    def display(self):
        print("Child Class Instance Method")


s = Son()
s.display()
s.show()
s.showMoney()

print(s.money)
s.money = s.money - 500
print(s.money)"""


# TODO: Constructor in Inheritance
""" class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor:", self.money)

    # def __init__(self, money):
    #     self.money = money
    #     print("Father Class Constructor:", self.money)

    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def __init__(self):
        super().__init__()
        self.tk = 500
        print("Son Class Constructor:", self.tk)

    # def __init__(self, money):
    #     super().__init__(money)
    #     self.tk = 500
    #     print("Son Class Constructor:", self.tk)

    def display(self):
        print("Son Class Instance Method")


s = Son()
 """


# TODO: Multi-level Inheritance
""" class Father:
    def __init__(self):
        print("Father Class Constructor")

    def showF(self):
        print("Father Class Method")


class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son Class Constructor")

    def showS(self):
        print("Son Class Method")


class GrandSon(Son):

    def __init__(self):
        super().__init__()
        print("GrandSon Class Constructor")

    def showG(self):
        print("GrandSon Class Method")


g = GrandSon()
g.showG()
g.showS()
g.showF() """


# TODO: Hierarchical Inheritance
""" class Father:
    def showF(self):
        print("Father Class Method")


class Son(Father):
    def showS(self):
        print("Son Class Method")


class Daughter(Father):
    def showD(self):
        print("Daughter Class Method")


s = Son()
s.showS()
 """


# TODO: Multiple Inheritance
""" class Father:
    def showF(self):
        print("Father Class Method")


class Mother:
    def showM(self):
        print("Mother Class Method")


class Son(Father, Mother):
    def showS(self):
        print("Son Class Method")


s = Son()
s.showF()
s.showM()
s.showS() """
