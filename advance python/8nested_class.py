class Army:  # Outer Class
    def __init__(self):
        self.name = "Rahul"
        self.gn = self.Gun()  # Inner Class Object

    def show(self):
        print(self.name)

    class Gun:  # Inner Class
        def __init__(self):
            self.name = "AK47"
            self.capacity = "75 Rounds"
            self.length = "34.3 in"

        def display(self):
            print(self.name, self.capacity, self.length)


a = Army()
a.gn.display()
print(type(a))

# b = a.Gun()
b = Army.Gun()
print(type(b))
