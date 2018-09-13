'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple
Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.
'''

def tuple_game(given_list):
    new_list = []
    sorted_list = sorted(given_list)
    # or given_list.sort -- doesn't return anything
    i = 0
    while i <= len(sorted_list) - 1:
        if len(sorted_list) / 2 != 0 and i == len(sorted_list) - 1:
            n_tuple = (sorted_list[i], 0)
        else:
            n_tuple = (sorted_list[i], sorted_list[i+1])
        new_list.append(n_tuple)
        i += 2
    return new_list

print(tuple_game([1, 3, 5, 4, 3, 1, 1]))
