# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

print "Welcome to the Guessing game"
user_input = int(raw_input("Guess a number that is 1-9"))
print user_input

import random
var = random.randint(1,9)
#print var

guess = 3
while guess > 0:
    guess -= 1
    if user_input == var:
        print "congratulations You've done it! "
        break
    if user_input < var:
        print "higher"
    if user_input > var:

        print "lower"
    user_input = int(raw_input("Guess a number that is 1-9"))


print var

user = raw_input('thanks for playing')
print user
exit(code=1)














