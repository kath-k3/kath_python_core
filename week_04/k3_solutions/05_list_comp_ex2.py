'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.
Then open up your online shop ;)
'''
# set of multiple sets

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

combined = [(size, color) for size in sizes for color in colors]
print(combined)

