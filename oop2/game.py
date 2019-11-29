import random

min_bound = 0
max_bound = 100
is_guessed = False
number = random.randint(min_bound, max_bound+1)
print (str(number))
print ("Welcome to the \"Guess The Number game\"!\nPlease enter the number:\nYou have 6 tries")
tries = 6
while not is_guessed:
    user_number = int(input())
    tries -= 1
    if tries > 0:
        print("You have " + str(tries) + " tries")

        if number == user_number:
            print("You guessed number!")
            break
        elif user_number < number:
            print("Your number is less than hidden number!")
        else:
            print ("Your number is greater than hidden number!")
    else:
        print("You lose the game!")
