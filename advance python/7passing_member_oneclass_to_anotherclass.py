class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)


class User:
    @staticmethod
    def show(s):
        s.display()


stu = Student("Rahul", 101)

User.show(stu)
