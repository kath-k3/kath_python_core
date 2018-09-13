'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.
Solution: http://thinkpython2.com/code/has_duplicates.py.
Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html
'''


def has_duplicates(given_list):
    dict = {}
    for i in given_list:
        if i in dict:
            return True
        dict[i] = True
    return False

print(has_duplicates([1, 2, 4, 3]))

# dict = {'1': True, '2': True} etc
# so we are using the values as keys and keys have to be unique?
