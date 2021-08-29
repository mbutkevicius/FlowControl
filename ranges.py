
for i in range(0, 10, 2):
    print("i is now {}".format(i))

# Here's an easier way
# for i in range(0, 10):
#     print("{}".format(i))

print()

for i in range(10):     # The range defaults to 0 if you don't provide a start value
    print(i)

print()

for i in range(0, 101, 7):      # the 7 shows how many steps to skip. It was like stepping in slices
    print(i)
    if i > 0 and i % 11 == 0:
        break

print()

for i in range(101)[::-7]:      # We can use negative stepping as well
    print(i)

print()

# for i in range(21):
#     if i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         continue
#     print(i)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
# Or we can do it without continue
print()

for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)