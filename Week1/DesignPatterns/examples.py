from abc import ABC, abstractmethod

# -----------------------------
# 1. Single Responsibility Principle (SRP)
# -----------------------------
class Report:
    def generate_report(self):
        print("Generating Report")

class ReportPrinter:
    def print_report(self):
        print("Printing Report")

# -----------------------------
# 2. Open/Closed Principle (OCP)
# -----------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 10 * 5

print("Circle Area:", Circle().area())
print("Rectangle Area:", Rectangle().area())

# -----------------------------
# 3. Liskov Substitution Principle (LSP)
# -----------------------------
class Bird:
    def move(self):
        print("Bird is moving")

class Sparrow(Bird):
    def move(self):
        print("Sparrow is flying")

bird = Sparrow()
bird.move()

# -----------------------------
# 4. Interface Segregation Principle (ISP)
# -----------------------------
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing Document")

    def scan_document(self):
        print("Scanning Document")

mfp = MultiFunctionPrinter()
mfp.print_document()
mfp.scan_document()

# -----------------------------
# 5. Dependency Inversion Principle (DIP)
# -----------------------------
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.drive()
