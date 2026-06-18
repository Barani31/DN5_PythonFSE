# SRP
class Report:
    def generate(self):
        print("Generating Report")

# OCP
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

obj = Circle()
print(obj.area())