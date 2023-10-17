print('Welcome date str!!')
numberof_date=int(input('how many date add? '))
date = []
for i in range(numberof_date):
    adddate = int(input("add the date: "))
    date.append(adddate)
    date.sort()
print("SUCCESSFULLY ADDED", date)

