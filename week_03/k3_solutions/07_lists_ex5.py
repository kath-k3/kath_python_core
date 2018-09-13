# Complete Exercise 10.3 (p.121) from the textbook.

# Write a function that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

def cumulative_list(given_list):
    cum_list = []
    total = 0
    for item in given_list:
        total += item
        cum_list.append(total)
    return cum_list

print(cumulative_list([1, 2, 3]))
