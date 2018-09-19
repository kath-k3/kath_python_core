'''
Build a simple aggregator function.
'''

# enumerate adds a counter to an iterable. Returns list of tuples.

my_list = [ "Monday", "Tuesday", "Wednesday"]

for ele in enumerate(my_list):
    print (ele)


# changing index
for count, ele in enumerate(my_list, 101):
    print (count, ele)
