# TODO constructor without parameter
class Mobile:
    def __init__(self):
        print("Mobile Constructor Called")
        self.model = "realme C17"


realme = Mobile()


# TODO constructor with parameter
class Mobile:
    def __init__(self, m):
        print("Mobile Constructor Called")
        self.model = m


realme = Mobile("realme C17")
