i = 1;
# while-loop
while i <= 10:
    print(i * "x")
    print(i)
    i += 1


# list
names = ["lud", "ckf", "yjw", "asf", "gad"]

print(names[0])
print(names[-1]) # -1 represents the last item in the list
print(names[0:3]) # prints items from index 0 to 3-1 (index 3 not inclusive)
print(names)


# list methods
# .append()
# .insert(index, anything) # insert at index
# .remove()
# len(names) # returns the size of the list

# for-loops
for name in names:
    print(name) # prints each name in new line

    