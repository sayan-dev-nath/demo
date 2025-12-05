# TODO: instance variable
"""
class Mobile:
    def __init__(self):
        self.model = "realme C17"  # instance variable

    def showModel(self):
        print(self.model)  # accessing instance variable


realme = Mobile()
"""


# TODO: class variable / static variable
class Mobile:
    fp = "Yes"  # class variable

    def __init__(self):
        self.model = "realme C17"

    def showModel(self):
        print(self.model)

    @classmethod
    def is_fp(cls):
        print(cls.fp)  # accessing class variable


realme = Mobile()
realme.showModel()

Mobile.is_fp()
