print("Welcome registration page !!")
number_of_user=int(input("How many users added: "))
user=[]
for i in range(number_of_user):
    adduser=str(input("Add user name: "))
    user.append(adduser)
print("successfully registered" ,user)
