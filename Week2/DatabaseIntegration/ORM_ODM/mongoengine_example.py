from mongoengine import *

connect("college")

class Student(Document):

    name=StringField()

    age=IntField()

student=Student(

name="Barani",

age=21

)

student.save()