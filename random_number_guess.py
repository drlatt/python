# guess a random number between 1 and 10
# let the user know if they're correct or not. Also let them know if the guess is too high or too low and let them guess again
# congratulate the user if the number is correct
# EXTRAS
# limit the number of guesses or tell them how many times they've guessed or both.

import random
random_num = random.randint(1,10)

################################################
#DEFINE FUNCTIONS
################################################
#generate a random number between 1 and 10
#def generate_random_number():
#    random_num = random.randint(1,10)

#prompt the user to guess the number that was generated
def guess_number():
    print("Enter a number between 1 and 10")
    #random_guess = input(">>> ")

#check to make sure that the number entered by the user is a number from 1 to 10
'''def check_num_range():
    if random_guess < "0" or random_guess > "10":
        print("The number you typed is out of requested range")
        #guess_number()
    else:
        # check if guessed number is correct or not
        compare_num()'''

#check if the number entered is equal to the number generated
def compare_num():
    if random_num != random_guess:
        print("Try again!!!")
    else:
        print("Congratulations on correct guess")

#execute the code
while True:
    print("Enter a number between 1 and 10")
    random_guess = input(">>> ")
    if random_guess < "0" or random_guess > "10":
        print("Number typed is not within allowed range, try again")
    else:
        compare_num()
