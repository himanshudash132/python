# Strings are immutable
a = "!!!!!!Harry !!!!!!!!!! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("!!!"))

print(str1.endswith("to",4,10))

str1 = "He's name is dan. he is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcometotheConsole"
print(str1.isalnum())

str1 = "Welcome00"
print(str1.isalpha())
print(str1.islower())
print(str1.isupper())

str1 = "We wish you a Merry christmas\n"
print(str1)
print(str1.isprintable())

str1 = "        " #using Spacebar
print(str1.isspace())

str2 = " " #using tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "fly Mocking bird"
print(str2.istitle())

str2 = "fly Mocking bird"
print(str2.startswith("Python"))



