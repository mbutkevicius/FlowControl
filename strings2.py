number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split() #this won't make sense yet
print([int(val) for val in values])

print()

number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split() #this won't make sense yet
print(sum([int(val) for val in values]))