# Complete Exercise 8.4 (p.80)
# Modify find so that it has a third parameter, the index in word where it should start looking.

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def find_mod(word, letter, start_index):
    while start_index < len(word):
        if word[start_index] == letter:
            return start_index
        start_index = start_index + 1
    return -1

print (find_mod("banana", "a", 4))
