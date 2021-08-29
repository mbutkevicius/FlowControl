import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:      # Can use multiple "if" statements
        print("You suck. Game over")
    elif guess < answer:
        print("Please try again and guess higher")
    else:
        print("Please try again and guess lower")
    guess = int(input())
print("Well done, you guessed it!")


# I JUST COMMENTED THIS OUT SO I COULD PRACTICE WHILE LOOPS

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed it")
# else:
# print("You got it the first time!")

# THIS IS INEFFICIENT CODE

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first try!")