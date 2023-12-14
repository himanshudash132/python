# import cv2
# import math

# # This is a comment
# print("Hello world")
# print(math.gcd(3,6))
'''
This is a multi line comment

'''
# This is also a comment
# print(5+8)
# if(age<18):
#     print("hello")


# a = 34
# b = "Harry"
# c = 45.32
# d = 3

# print(a + d)
# print(a - d)
# print(a * d)
# print(a / d)


# Wrong syntax
# harry project = 45 
# Rules for creating variables

# 1. variable should start with a letter or an underscore
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive. Harry and harry are two different variables



# typeA = type(a)
# typeB = type(b)
# print(typeA)

# e = "31"
# e = float(e)
# e = str(e)
# e = str(e)


# e = 3.14
# prfnt(type(e))
# prfnt(e+2)


# s = "56.7"
# i = 43

# i=float(i)
# print(i)

# i=str(i)
# print(i)

# s = "56.7"

# s=float(s)
# print(s)

# s=int(s)
# print(s)

# f = 34.0
# f=int(f)
# print(f)

# f=str(f)
# print(f)
# 01234
# name = "Harry, shubham, vikrant"
# is a good boy
# print(name[2:5])
# print(name.strip())
# print(len(name))
# var = name.lower()
# var = name.upper()
# var = name.replace("ar","t")
# var = name.replace(", ","\n")
# print(var)

# stri = "This is a "
# name1 = "Harry"
# name2 = "Rohan"
# stri2 = "This is not a"
# # print(stri + name)
# # temp = " This is a {1} and he is a good boy named {0}".format(name1, name2)
# temp = f"this is a {name2} and he is a good boy {name1}"
# print(temp)

# quiz
# 1 ** Exponentiation operator
# 2 // Floor division operator
# 3 % Modulo operator

# print(3**2)
# print(3//2)
# print(3%2)

'''

python Collections:
1.List
2.Tuples
3.Set
4.Dictionary

'''

# [List] ---->is mutable


# lst = [61, 2, 3, 4, 6, 41]
# # var = type(lst)
# # lst[2] = 45
# # var = lst[2]
# # lst.append(100)
# # lst.insert(0, 100)
# # lst.remove(61)
# # lst.pop()
# # del lst[3]
# # del lst
# lst.clear()
# var = lst
# # var = len(lst)
# # var = lst[1:4]
# print(var)

# (Tuple) ----> immutable

# a = ("Harry","Shubh","Rohan")
# # var = a
# a = list(a)
# var = type(a)
# cannot do this
# a[0] = "vikrant" 
# print(var)

# H.w 😊


# tup = (22, 45, 23, 78, 6.89)
# print(len(tup))
# print(tup.count(23))
# print(tup.index(23))
# print(sum(tup))
# print(min(tup))
# print(max(tup))


# Set removes repeated elements ,  it is unorderded and  no indexing  
# # s1 = {23,2,2,2,2,2,7,12,5,2,272,2,2,2}
# # print(23 in s1)
# # s1.add(444444)
# # s1.update([12,12,423,3423,632,123,432,23])
# # print(len(s1))
# # s1.remove(23) # remove 23 if present or if not present  return an error
# # s1.discard(1) # remove 23 if present or if not present does not return an error
# # s1.pop()  # remove  the last element from the set
# # s1.clear()


# print(s1)


# A = { 1,2,3,4,5}
# B = { 2,4,6,8}

# print("union", A|B)

# print("intersection", A&B)

# print("difference", A-B)

# print("Symmetric difference :", A ^ B)



# Dictionary

# harrydict = {
#     "Name": "Harry ",
#     "Class":"4th",
#     "Marks":34.34,
#     "Hours In School": 6
# }

# harrydict["Marks"] =39 # add an item with "39" as key and "34.34" as its value
# print(harrydict["Marks"])

# print(harrydict)
# print(len(harrydict))

# del harrydict["Marks"] # delete item having "Marks" key
# print(harrydict)

# harrydict.clear()#If we need to remove all items from the dictionary at once, we can use the clear() method.
# print(harrydict)

# harrydict.pop("Marks")
# print(harrydict)

# harrydict2 = {
#     "Name": "Harry2 ",
#     "Class":"5th",
#     "Marks":99.34,
#     "Hours In School": 7
# }
# harrydict.update(harrydict2)

# print(harrydict)

# age = int(input("Enter Your age"))
# age = int(age)
# print(type(age))

# conditions  statement

# age = int(input("Enter Your age ="))
# # print(type(age))

# if(age>18):
#     print("You can drive a car\n")

# elif(age==18):
#     print("You can drive a car\n")
# else:
#     print("You cannot drive\n")   

# loops
 
# for i in range(0,1000):
#     print("i") 
   
# li = [1 , 432, "this"]
# for item in li:
#     print(item)

# s1 = {23,2,2,2,2,2,7,12,5,2,272,2,2,2}
# for i in s1:
#     print(i)

# harrydict2 = {
#     "Name": "Harry2 ",
#     "Class":"5th",
#     "Marks":99.34,
#     "Hours In School": 7
# }
# for i in harrydict2:
#     print(i)        
    
# tup = (22, 45, 23, 78, 6.89)
# for item in tup:
#     print(item)

# i = 0 # break
# while(i<100):
#     i+=1
#     if i == 78:
#         continue
#     print(i+1)


# def greetHello(name, ending):
#     print("hello " + name) 
#     print("hello") 
#     print("hello") 
#     print("hello")
#     print(ending)

# def letterGenerator(name, date):
#     st = f"Hi mam,\nThis is {name} and i will not come to school on {date}" 
#     print(st)   


# def average(a,b):
#     return (a+b)/2    

# print("Executing Function...")
# greetHello("Harry", "Thank You")
# greetHello("Rahul", "Thanks")
# letterGenerator("Harry", "26th Oct")
# letterGenerator("Rahul", "27th Oct")
# print(average(34,54))
# print("done")    








# try:
#     a = int(input("Enter your number"))

#     print(a+3)
# except Exception as e:
#     print("some error occured:", e)    



# s = "Harry is a good boy"
# # x is used to create a file which does not exist 
# with open("text.txt", "x") as f:
#     f.write(s)

# fp = open("text.txt", "x")
# fp.write(s)
# fp.close()

# #  Writing to a file


# with open("text.txt", "w") as f:
#     f.write(s)

# fp = open("text.txt", "w")
# fp.write(s)
# fp.close()

# # Reading a file


# with open("text.txt", "r") as f:
#     f.read()
#     print(s)


# fp = open("text.txt", "r")
# fp.read()
# print(s)
# fp.close()


# # Appending to a file


# with open("text.txt", "a") as f:
#     f.write("\nhimanshu is a good boy\n")

# fp = open("text.txt", "w")
# fp.write(s)
# fp.close()


#  CLASS 

# class Employee:
#     # salary = 89
#     # name = "Rahul"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def getSalary(self):
#         print( self.salary)

#     def getname(self):
#         print( self.name)

# rahul = Employee("Rahul", "300000")
# # print(rahul.salary)    
# # print(rahul.name)
# rahul.getSalary()  
# rahul.getname()  

# himanshu = Employee("Himanshu", "3000000000000000000000000000")
# # print(himanshu.salary)    
# # print(himanshu.name)
# himanshu.getSalary()    
# himanshu.getname() 

# class Employee:
#     salary = 89
#     name = "Rahul"

# rahul = Employee()
# print(rahul.salary)    
# print(rahul.name)    