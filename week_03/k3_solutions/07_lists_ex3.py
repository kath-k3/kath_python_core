#Complete Exercise 10.1 (p.120) from the textbook.
#Sum up all elements from a nested list of integers.

# Ex 10.1. Write a function called nested_sum that takes a nested list of integers
# and add up the elements from all of the nested lists.


def nested_sum(given_list):
    n_sum = 0
    for item in given_list:
        if type(item) == list:
            n_sum += sum(item)
        else:
            n_sum += item
    return n_sum

print(nested_sum([1, 2, 3, [2, 3]]))
