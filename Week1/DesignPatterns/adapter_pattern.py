class OldPrinter:
    
    def print_old(self):
        print("Old Printer")

class Adapter:

    def __init__(self, printer):
        self.printer = printer

    def print(self):
        self.printer.print_old()

obj = Adapter(OldPrinter())
obj.print()