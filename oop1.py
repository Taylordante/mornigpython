class Employee:

    #Attributes
    def __init__(self,fullname,position,status,age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print(self.fullname,"Is working")

employee1 = Employee("Ahmed Mziza","Cleaner","Married","40")
print(employee1.fullname,employee1.position,employee1.status,employee1.age)
employee1.work()
employee2 = Employee("Marley Mreta","Watchman","Single","34")
print(employee2.fullname,employee2.position,employee2.status,employee2.age)
employee2.work()
employee3 = Employee("Dante Mzii","Cook","Married","45")
print(employee3.fullname,employee3.position,employee3.status,employee3.age)
employee3.work()



