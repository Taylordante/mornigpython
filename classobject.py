
#Class is a blueprint of an object.
#Object is an instance of a class


class student:
    #Attributes
    name = "Mreta"
    age = 23
    gender = "Male"
    course = "MIT"
    weightvalue = 78

   #Behaviour/Functions
    def study(self):
         print("Student is studying")

student1 = student() #Creating an object
student1.study()
print(student1.name)

student2 = student
student1.study()
print(student1.name)


student3 = student
student1.study()
print(student1.name)










