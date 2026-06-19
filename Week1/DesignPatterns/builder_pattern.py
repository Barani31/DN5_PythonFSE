class Computer:
    
    def __init__(self):
        self.cpu = ""
        self.ram = ""

    def show(self):
        print(self.cpu, self.ram)

c = Computer()

c.cpu = "i7"
c.ram = "16GB"

c.show()