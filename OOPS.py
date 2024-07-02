# Object and Class
# class Student:
#     name="Navneet"

# s1=Student()
# print(s1.name)
# <-------------------------->

# Constructor
# class Student:
#     name="Navneet"
#     def __init__(self):
#         print("New Student is Comming")

# s1=Student()

# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("New Student is Comming")

# s1=Student("Navneet Kumar Singh")
# print(s1.name)
# <------------------------------->

# Methods are function that belong to object
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("Welcome Bro",self.name)
# s1=Student("Navneet",97)
# s1.welcome()
# <-------------------------------->

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is:",sum/3)
         
# s1=Student("Navneet",[97,89,92])
# s1.avg()

# s1.name="DON"
# s1.avg()
# <------------------------------------>

# Static Methods
# Static method is define by the symbol of@
# <------------------------------------->

# Abstraction
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car is started")

# car1=Car()
# car1.start()

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount, "was debited")
        print("total balance = ",self.getbalance())
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount, "was credited")
        print("total balance = ",self.getbalance())
    
    def getbalance(self):
        return self.balance

acc1=Account(1366562,123)
# print(acc1.balance)
# print(acc1.account)   
acc1.debit(1000)
acc1.credit(500)

