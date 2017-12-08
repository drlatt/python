
import random
guessed_nums = []
chances = []
total_guess = 5

random_num = random.randint(1,10)

while len(chances) < total_guess:
    random_guess = input("Print enter a number between from 1 to 10: ")
    try:
        picked_num = int(random_guess)
    except:
        print("That's not a whole number")
        break
    if not picked_num > 0 or not picked_num < 11:
        print("The number you entered is not within allowed range")
        break
    chances.append(random_guess)

    if picked_num < random_num:
        print("Your guess is lower than the random number")
    elif picked_num > random_num:
        print("Your guess is higher than the random number")
    else:
        print("Your guess is correct and equal to the random number {}".format(random_num))
        break
