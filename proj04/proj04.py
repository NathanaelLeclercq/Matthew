# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

user_input = raw_input("What word would you like to know if it is a palindrome ?")
print user_input
word = user_input
stringList = []
for letter in word:
    stringList.append(letter)

print stringList

while word:
    if word[0] == word[-1]:
        word = word[1:-1]

    else:
        print "Not a palindrome."
        break


