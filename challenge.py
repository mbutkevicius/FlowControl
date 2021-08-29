# I think I could just use triple quotes instead of '\'
menu = "Please choose your options from the list below:\n\
1.\tPlay games\n\
2.\tStudy Japanese\n\
3.\tPractice Coding\n\
4.\tExercise\n\
0.\tExit"

print(menu)

while True:
    activity = input()

    if activity == "0":
        print("Goodbye")
        break
    elif activity in "1234":
        print("You chose {}".format(activity))
    else:
        print(menu)

# print("Please choose your options from the list below:")
# print("1.\tPlay games")
# print("2.\tStudy Japanese")
# print("3.\tPractice Coding")
# print("4.\tExercise")
# print("0.\tExit")
# This was my first attempt.  I was using int instead of strings
# while True:
#     activity = int(input())
#     if activity != 0 and activity < 5:
#         print("That sounds like a lot of fun!")
#     if activity > 4:
#         # print("Please choose a valid option")  Whoops that wasn't the challenge
#         print("Please choose your options from the list below:")
#         print("1.\tPlay games")
#         print("2.\tStudy Japanese")
#         print("3.\tPractice Coding")
#         print("4.\tExercise")
#         print("0.\tExit")
#     if activity == 0:
#         print("Goodbye")
#         break

# This was his solution to optional challenge:

# choice = "-"
# while True:
#     if choice == "0":
#         break
#     elif choice in "1234":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your options from the list below:")
#         print("1.\tPlay games")
#         print("2.\tStudy Japanese")
#         print("3.\tPractice Coding")
#         print("4.\tExercise")
#         print("0.\tExit")
#
#     choice = input()

# Or we can do it without the while True loop and add a variable

# choice = "-"
# while choice != "0":
#     if choice in "1234":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your options from the list below:")
#         print("1.\tPlay games")
#         print("2.\tStudy Japanese")
#         print("3.\tPractice Coding")
#         print("4.\tExercise")
#         print("0.\tExit")
#
#     choice = input()