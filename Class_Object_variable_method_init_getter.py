class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def print_info(self):
        print(f"Your name is {self.name}, and you are {self.age} years old!")

    def birthday(self):
        print("Happy Birthday!!")
        self.age += 1


mohammad = Person("Mohammad", 34)
print(mohammad.get_name(), mohammad.get_age())
mohammad.print_info()
mohammad.birthday()
mohammad.print_info()

