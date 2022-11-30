# numbers
# strings
# boolean
# etc

year = input("Enter your birth year: ")
# age = year - 2020 # this is wrong. need typecasting
age = 2022 - int(year) # this is how we can typecast

print("Your age is: " + str(age) + "\n")

# typecasting methods
# int()
# float()
# bool()
# str()

# calc exer - typecasting basics
n1 = float(input("First: "))
n2 = float(input("Second: "))
sum = n1 + n2
print("Sum: " + str(sum))