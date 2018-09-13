# Exercise 10.8. The (so-called) Birthday Paradox:
# 1. Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should not modify the original list.
# 2. If there are 23 students in your class, what are the chances that two of you have the same birthday?
# You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
# Hint: you can generate random birthdays with the randint function in the random module.


def has_duplicates(g_list):
    item_index = 0
    while item_index <= len(g_list) - 1:
        item_index2 = item_index + 1
        while item_index2 <= len(g_list) - 1:
            if g_list[item_index] == g_list[item_index2]:
                return True
            item_index2 += 1
        item_index += 1
    return False

print(has_duplicates([1, 5, 2, 3]))
