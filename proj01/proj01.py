# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

user_input = raw_input("Enter a name: ")
print user_input
user_input2 = raw_input("Enter your age: ")
print user_input2
year100 = 100 - int(user_input2) + int(user_input2)
year2000 = year100 + 2000
user_input3 = raw_input("Have you had you birthday yet, press 0 if yes or press 1 if no ? ")
print user_input3

if user_input3 < int(1):

    print "You will be 100 in"
    print (year2000 - 1)
    print "years."
else:
    print "You will be 100 in"
    print (year2000)
    print "years"


