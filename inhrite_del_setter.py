class Computer:
    count = 0

    def __init__(self, cpu, gpu, ram, hard):
        Computer.count += 1
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.hard = hard

    def get_value(self):
        return self.cpu + self.gpu + self.ram + self.hard

    def __del__(self):
        Computer.count -= 1


class Laptop(Computer):
    def get_value(self):
        return self.cpu + self.gpu + self.ram + self.hard + self.battery


pc1 = Computer(2, 2, 4, 2)
print(pc1.get_value())

laptop1 = Laptop(2, 4, 4, 2)
laptop1.battery = 4
print(laptop1.get_value())

print(Computer.count)
laptop1.__del__()
print(Computer.count)

