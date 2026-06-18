class Add:
    def execute(self,a,b):
        return a+b

class Multiply:
    def execute(self,a,b):
        return a*b

obj=Add()
print(obj.execute(10,20))

obj=Multiply()
print(obj.execute(10,20))