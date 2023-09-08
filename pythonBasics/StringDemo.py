str = "EmilyDu.com"
str1 = "Consulting firm"
str3 = "EmilyDu"
str31 = "EmilyBX"
print(str[1])  # a
print(str[0:5])  # Emily
print(str + " " + str1)  # concatenation
print(str3 in str)  # True
print(str31 in str)  # False substring check
var = str.split(".")
print(var)
print(var[0])
str4 = " great "
print(str4.strip())  # great No white space neither on left nor on right
print(str4.lstrip())  # great  No white space on left
print(str4.rstrip())  #  great No white space on right