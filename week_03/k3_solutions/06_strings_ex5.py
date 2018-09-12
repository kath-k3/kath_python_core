# Write a script that takes a user inputed string
# and prints it out in the following three formats.
#   - All letters capitalized.
#   - All letters lower case.
#   - All vowels lower case and all consonants upper case.


user_input = input("Give me a string please: ")

def lower_upper_input(given_string):
    print (given_string.upper(), given_string.lower())


vowels = ['a', 'e', 'i', 'o', 'u']
def vow_con(user_input):
    '''Returns new string with vowels lower case and consonants upper case'''
    new_string = ''
    for letter in user_input:
        if letter in vowels:
            new_string += (letter.lower())
        else:
            new_string += (letter.upper())
    return new_string


lower_upper_input(user_input)
print (vow_con(user_input))
