s1 = "this is a message" # this is a string object

# we can use the dot operator to access the string methods
# python is case-sensitive
# STRINGS ARE IMMUTABLE

s1up = s1.upper()
i = s1.find("t") # returns the index of the first found instance
i2 = s1.find("message")


# other methods:
# .replace()
# .find()



print(s1up + " in uppercase.")
print(i)
print(i2)
print("hello" in s1) #using the in-operator
print("messag" in s1)