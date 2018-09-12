#Write a script that finds the first vowel in a a user inputted string.


user_string = input("Could you give me a string please? ")

vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    for letter in user_string:
        if vowel == letter:
            print (vowel)

