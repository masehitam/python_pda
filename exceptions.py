class Exc0(Exception):
    def __init__(self):
        self.message = "Exc0 occurred"

    def __str__(self):
        return self.message


class Exc1(Exc0):
    def __init__(self):
        self.message = "Exc1 occurred"

    def __str__(self):
        return self.message


try:
    raise Exc1()
except Exc0 as e:
    print("Exc0 caught")
    print(e)
except Exception as e:
    print("Base exception caught")
    print(e)
finally:
    print("Finally done")

try:
    raise Exc1()
except Exc1 as e:
    print("Exc1 caught")
    print(e)
finally:
    print("Finally again")

print("End of program")
