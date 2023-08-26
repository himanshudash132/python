# Calculator

a = int(input(" Enter a ="))
b = int(input(" Enter b ="))
print("1 Addition  \n 2 Subtraction \n 3 Multiplication  \n 4 Division  \n 5 Floor division \n 6 Modulus  \n 7 Exponent ")
c = int(input(" Enter c ="))


if (c == 1):
    print("The valve of", a, "+" , b, "is", a+b)
elif (c == 2):
    print("The valve of", a, "-" , b, "is", a-b)
    print(a-b)
elif (c == 3):
    print("The valve of", a, "*" , b, "is", a*b)
    print(a*b)
elif (c == 4):
    print("The valve of", a, "/" , b, "is", a/b)
    print(a/b)
elif (c == 5):
    print("The valve of", a, "//" , b, "is", a//b)
    print(a//b)
elif (c == 6):
    print("The valve of", a, "%" , b, "is", a%b)
    print(a%b)
else:
    print("The valve of", a, "**" , b, "is", a**b)
    print(a**b)
