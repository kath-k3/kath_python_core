'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.
'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

div_1111 = (i for i in range(1, 1000000) if i%1111 == 0)

for i in div_1111:
    print(i)


