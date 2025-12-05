# class variable - namespace
class Mobile:
    fp = "Yes"

    @classmethod
    def is_fp(cls):
        print("Finger Print:", cls.fp)


realme = Mobile()
redmi = Mobile()
geek = Mobile()

Mobile.fp
print(Mobile.fp)
print(realme.fp)

Mobile.fp = "No"
print(Mobile.fp)
print(realme.fp)
