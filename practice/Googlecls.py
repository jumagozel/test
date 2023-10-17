# class Google():
#     def __init__(self):
#         pass
#     users=[]
#     def googlemeet(self):
#         for i in range(3):
#             user1=(input("google meet user: "))
#             self.users.append(user1)
#         print(self.users)
# x=Google()
# x.googlemeet()

class Employee():
    # print("Welcome Bootcamp employee:")
    def __init__(self):
        pass
    def Register(self):
        f=open("registr.txt", "w")
        while True:
            self.name=(input("enter your name: "))
            self.age=(input("enter your age: "))
            self.language=(input("language: "))
            self.position=(input("enter your position: "))
            print("Are you sure you want to exit from this ?")
            self.are_you_exit=input(">>> ").lower()
            f.write(f"{self.name}\n {self.age}\n {self.language}\n {self.position}")
            if self.are_you_exit=="yes":
                break
        f.close()
output=Employee()
output.Register()