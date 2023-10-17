# how mane even and odd number
# number=int(input("how many number:"))
# even_count=0
# odd_count=0
# numbers = []
# for i in range(number):
#     addnumber = int(input("add the number: "))
#     numbers.append(addnumber)
#     if addnumber%2!=1:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1
# print('odd', odd_count)
# print('even', even_count)

# 2-nji ish
# s=input('input a string: ')
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         print("error input")
# print("Letters", l)
# print("Digits", d)

# 2-nji ish 2-nji wariant

s=input("Enter a string: ")
letters = 0
digits = 0

for char in s:
    char_ascii = ord(char)
    if 65 <= char_ascii<=90 or 97 <=char_ascii<=122:
        letters+=1
    elif 48<=char_ascii<=57:
        digits+=1

print("Number of letters: ", letters)
print("number of digits: ", digits)


