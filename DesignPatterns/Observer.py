class Student:
    def update(self,msg):
        print(msg)

class Teacher:
    def __init__(self):
        self.students=[]

    def add(self,s):
        self.students.append(s)

    def notify(self,msg):
        for i in self.students:
            i.update(msg)

s1=Student()
s2=Student()

t=Teacher()
t.add(s1)
t.add(s2)

t.notify("Exam Tomorrow")