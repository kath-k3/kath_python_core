# Write a script that takes a user inputed string
# and prints it out in the following three formats.
#   - All letters capitalized.
#   - All letters lower case.
#   - All vowels lower case and all consonants upper case.


user_input = input("Give me a string please: ")

def lower_upper_input(given_string):
    given_string = user_input
    print (given_string.upper(), given_string.lower())


vowels = ['a', 'e', 'i', 'o', 'u']
def vow_con(user_input):
    for letter in user_input:
        if letter in vowels:
            print (letter.lower())
        else:
            print (letter.upper())


lower_upper_input()

