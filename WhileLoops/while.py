#for i in range(10):
#    print("i is now {0}".format(i))

# i =0
# while i< 10:
#     print(" i is now  {0}".format(i))
#     i += 1


# available_exits = ["east","west","south","north"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction :")
#     if chosen_exit == "quit":
#         print("GAME OVER")
#         break
# else:
#     print("aren't you glad that you got out")

import random

highest = 100
answer = random.randint(1,highest)

print("Please guess a number between 1 and {0}:".format(highest))
guess = 0
#if guess != answer:
while guess!= answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    #guess = int(input())
    #if guess == answer:
    else:
        print("You guessed correctly")
    # else:
    #     print("Incorrect guess:")
    #     #print("Number is {0}".format(answer))
# else:
#     print("1st time you got it")