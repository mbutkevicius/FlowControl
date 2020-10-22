name = input("What is your name: ")
age = int(input("How old are you, {}: ".format(name)))
under = "youngin"
over = "old man"

if 18 <= age < 31:
    print("Congratulations! Welcome to your free holiday, {}!".format(name))
elif 18 > age:
    print("Crawl back in the womb, {}".format(under))
else:
    print("Get lost {}".format(over))