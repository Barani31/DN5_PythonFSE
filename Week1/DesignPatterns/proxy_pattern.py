class RealImage:
    
    def display(self):
        print("Displaying Image")

class ProxyImage:

    def __init__(self):
        self.real = RealImage()

    def display(self):
        print("Proxy Access")
        self.real.display()

obj = ProxyImage()
obj.display()