from students.models import Student

Student.objects.create(

name="Barani",

age=21

)

Student.objects.all()

Student.objects.filter(age=21)

Student.objects.get(id=1)

Student.objects.update(age=22)

Student.objects.delete()