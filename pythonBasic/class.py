# class Bootcamp():
#     print("Hi Bootcamp")

# print(Bootcamp)

# class SomeOperation():
#     x=10
#     y=30
#     sum=x+y
# new1=SomeOperation()
# new=SomeOperation()
# item=new.sum
# item2=new1.y
# print(item)
# print(item2)

# #################### class 3 soramaly
# class Person():  
#     def __init__(self,name,lastname):
#         self.name=name
#         self.lastname=lastname
    
#     def __str__(self):
#         f"hi{self.name} {self.lastname}"


# item=Person("Python", "Pythonov")
# print(item.name)
# print(item.lastname)
# # print(item)

# class Person():  
#     def __init__(self,name,lastname,number):
#         self.name=name
#         self.lastname=lastname
#         self.number=number
    
#     def __str__(self):
#        self.number+=1
#        return f"hi{self.name} {self.lastname} number{self.number}"

#     def hitext(self):
#         return f"Welcome{self.name} "

# item=Person("Python", "Pythonov", 7890)
# print(item)
# print(item.hitext)

# class University():
#     def __init__(self,name):
#         self.name=name

#     def Uname(self,sortname):
#         new=f"Welcome{self.name} university of Turkmenistan({sortname})"
#         return new 

# Uni=University("Oguzhan Engineering and Technology")
# print(Uni.Uname("TITU"))
# del Uni

# class Person():
#     def __init__(self,name,lastname):
#         self.name=name
#         self.lastname=lastname
        #   self.age=23 #age

#     def somefunctions(self):
        #   new=f"hi {self.lastname} my age {self.age}"
#         return new
        
# class Student(Person):
#     def __init__(self,name,lastname):
#         Person.__init__(self,name,lastname)

# value=Student("Python", "Student")
# print(value.name, value.lastname)
# print(value.somefunctions())


class Person():
        def __init__(self,name,lastname):
                self.name=name
                self.lastname=lastname
        
        def lastyear(self):
                print(f"welcome{self.name}")

class Student(Person):
        def __init__(self,name,lastname):
                super().__init__(name,lastname)
                self.gyear=2024
item=Student("allamyrat", "annayew")
item1=item.lastyear()


