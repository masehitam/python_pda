class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Dog(Mammal):
    def __init__(self, name, age, breed):
        Mammal.__init__(self,name,age)
        #super().__init__(name, age)
        self.breed = breed

    def get_breed(self):
        return self.breed

    def __str__(self):
        return f"My name is {self.name} and my breed is {self.breed}"

print(Dog("Wiwid", 3, "Labrador"))