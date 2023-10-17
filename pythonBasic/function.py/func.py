# def Hello(name, lastname):
#     print("Hello" + " " + name + " " + lastname)
    # # let's learn about functions
# def Hello():
    
#     print("Hi There!")

# Hello()


# def Hello(name,lastname):
#     print("Hello" +" " + name +""+ lastname)


# Hello("Python","C++")

# def greeting(*value):
#     print("Hello " + value[1] + value[0])

# greeting("Python","C++","Javascript")

# def hello(python,cv,js):
#     print("Hello " + python)
#     print("Hello " + cv)
#     print("Hello " + js)


# hello(python ="Python",cv="C++",js="Javascript")
# hello(python ="Python1",cv="C++1",js="Javascript1")


# def hello(**value):
#     print("Hello " + value["python"])



# hello(python ="Python",cv="C++",js="Javascript")

# def week(day="Monday"):
#     print("Week " + day)

# week("Thursday")
# week("Friday")
# week("Wednesday")
# week()

# value=["apple", "orange", "cherry"]
# def fruits(food):
#     for i in food:
#         print(i)

# fruits(value)'

# def same_ex(value):
#     sum=value+value
#     return sum


# #same_ex(5)
# print(same_ex(5))


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# def function(value):
#     sum=value+value
#     print("Result ",sum)

# function(5)
# #######################################
# def procodure(value):
#     sum=value+value
#     return sum

# print(procodure(5))

# def PowerA3(A):
#     B = A**3
#     return B


# for i in range(5):
#     number = int(input("enter number: "))
#     result = PowerA3(number)
#     print(result)

# def Mean(X, Y):
#     Amean = (X+Y)/2
#     Gmean = pow((X*Y), (1/2))
#     return Amean, Gmean


# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
# D = int(input("D: "))

# print("A and B", Mean(A, B))
# print("A and C", Mean(A, C))
# print("A and D", Mean(A, D))

################################ proc5 #######################################
# def RectPS(x1,x2,y1,y2):
#     side1=abs(x2-x1)
#     side2=abs(y2-y1)
#     P=2*(side1+side2)
#     S=side1*side2
#     return P, S

# for i in range(3):
#     x1 = int(input("enter x1: "))
#     x2 = int(input("enter x2: "))
#     y1 = int(input("enter y1: "))
#     y2 = int(input("enter y2: "))
#     result=RectPS(x1,x2,y1,y2)
#     print("Result", result)

##################################### proc 6 ##################################

# def digitCount(K): 
#     l=0
#     n=str(K)
#     c=len(n)
#     print("count: ", c)
#     for i in n:
#         m=int(i)
#         l=l+m
#     print(l)


# for i in range(5):
#     K=int(input("enter the number: "))
#     digitCount(K)

################################### proc 11 ######################################

################################### proc 12 #####################################


# def SortInc (A, B, C):
#     pass
#     if A<B and B<C and A<C:
#         pass
#         print(A,B,C)
#     elif B<A and B<C and A<C:
#         pass
#         print(B,A,C)
#     elif C<B and C<A and B<A:
#         pass
#         print(C,B,A)

# for i in range(2):
#     A=int(input("enter the number: "))
#     B=int(input("enter the number: "))
#     C=int(input("enter the number: "))
#     SortInc(A, B, C)

# A=int(input("A: "))
# B=int(input("A: "))
# C=int(input("A: "))

# def SortInc(A, B, C):
#     if A>B:
#         A, B = B, A
#     if B>C:
#         B, C = C, B
#     if A>B:
#         A,B = B,A
#     return A, B, C
# print(SortInc(A, B, C))

###################################### proc 16 ##################################
x=int(input("enter the number: "))
def sinx(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    else: 
        return 1
first = sinx(x)
# second = sinx(x)
# result=first+second

print(first)