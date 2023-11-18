class School:
    count = 0

    def __init__(self):
        self.number = int(input("Please Enter Your Number: "))
        self.data = []
        self.age = self.set_info("ages")
        self.height = self.set_info("heights")
        self.weight = self.set_info("weights")

    def set_info(self, title):
        self.data = (input(f"Please enter {title}: ").split())
        for j in range(self.number):
            self.data[j] = int(self.data[j])
        return self.data

    def avg_age(self):
        return sum(self.age)/self.number

    def avg_height(self):
        return sum(self.height)/self.number

    def avg_weight(self):
        return sum(self.weight)/self.number


a = School()
b = School()

print(a.avg_age())
print(a.avg_height())
print(a.avg_weight())
print(b.avg_age())
print(b.avg_height())
print(b.avg_weight())
if a.height > b.height:
    print("A")
elif a.height < b.height:
    print("B")
elif a.weight < b.weight:
    print("A")
elif a.weight > b.weight:
    print("B")
else:
    print("SAME")



