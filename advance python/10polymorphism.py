# TODO: Duck Typing
"""class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")


class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")


d = Duck()
d.walk()

d = Horse()
d.walk()"""


# TODO: Strong Typing
"""class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")


class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")


class Cat:
    def talk(self):
        print("meow meow")


def myfunction(ob):
    if hasattr(ob, "walk"):
        ob.walk()


d = Duck()
myfunction(d)

c = Cat()
myfunction(c)"""


# TODO: Method Overloading
"""class Myclass:
    def sum(self, a):
        print("1st Sum Method", a)

    def sum(self):
        print("2nd Sum Method")


obj = Myclass()
obj.sum(10)
obj.sum()"""


# TODO: Method Overriding
"""class Add:
    def result(self, a, b):
        print("Addition:", a + b)


class Multi(Add):
    def result(self, a, b):
        super().result(a, b)
        print("Multiplication:", a * b)


m = Multi()
m.result(10, 20)"""

# TODO: Operator Overloading
