import random

guessTaken = 0
print("Hello!What's your name?")
User_name = input()
number = random.randint(1, 21)
print("Well," + User_name + "I am thinking of a number between 1 and 20.\nTake a guess.")

while guessTaken < 6:
    print("Take a guess.")
    guess = input("请输入0到20的数字：")
    guess = int(guess)

    guessTaken += 1

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")

    else:
         print("Congratulation!{0}You are right!".format(User_name))