# Complete exercises in section 8.7 (p.75)

# ex8.5
#The following program counts the number of times the letter a appears in a string:
#word = 'banana'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#print count

#Encapsulate this code in a function named count,
#and generalize it so that it accepts the string and the letter as arguments.

def letter_count_1(q_letter, q_word):
    '''Counts occurrances of a given letter in a given string'''
    count = 0
    for letter in q_word:
        if q_letter == letter:
            count += 1
    return count

#print (letter_count_1('a', 'dragon'))


# ex8.6
#Rewrite this function so that instead of traversing the string,
#it uses the three- parameter version of find from the previous section.

def letter_count_2(q_letter, q_word, q_index):
    '''Returns the True if a given letter is in the given word at required index'''
    while q_index < len(q_word):
        for letter in q_word:
            if q_letter == q_word[q_index]:
                return True
            else:
                return False
        q_index += 1

print(letter_count_2('r', 'dragon', 1))


# ex8.7

word = 'banana'

def letter_count_3(q_letter):
    '''Counts occurrances of given letter in a certain string'''
    count = 0
    for letter in word:
        if q_letter == letter:
            count += 1
    return count

#print (letter_count_3('a'))


