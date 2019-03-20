str1='hello world , my complex world !'
print(str1.find('world'))
print(str1.rfind('world'))
print(str1.count('world'))
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.title())
print(str1.swapcase())
str2="Hey hey , u can't catch me"
print(str2.swapcase())
print(str1.replace('world','kid'))
str3 = "    yaaaaaaaa     "
print(str3.lstrip())
print(str3.rstrip())
print(str3.strip())
str4 = "Gaaaaaa"
width = 20
print(str4.ljust(width))
print(str4.center(20))
print(str4.rjust(20))