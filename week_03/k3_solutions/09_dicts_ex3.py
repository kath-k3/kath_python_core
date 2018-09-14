'''
Write a script that takes a sentence from the user and returns:
- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters
Use a dictionary to store the count of each of the above.
Note: ignore all spaces.
Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1
'''
u_s = input("Can you give me a sentence please: ")

def find_the_count(given_sentence):
    results_dict = {}
    lower_letters = 0
    upper_letters = 0
    puncts = 0
    for i in given_sentence:
        if i.islower():
            lower_letters += 1
        elif i.isupper():
            upper_letters += 1
        elif i == ' ':
            continue
        else:
            puncts += 1
    results_dict['Upper case: '] = upper_letters
    results_dict['Lower case:'] = lower_letters
    results_dict['Punctuation'] = puncts
    #That is wrong: results_dict.update('Upper case: ': upper_letters, 'Lower case: ': lower_letters, 'Punctuation: ': puncts)
    return results_dict

print(find_the_count(u_s))
