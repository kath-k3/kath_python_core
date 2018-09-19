'''
Use a one-line list comprehension to express the following functionality:
letters = []
for letter in 'suchalongword':
    letters.append(letter)
print(letters)
'''

old_string = 'suchalongword'
letters = [letter for letter in old_string]

print(letters)
