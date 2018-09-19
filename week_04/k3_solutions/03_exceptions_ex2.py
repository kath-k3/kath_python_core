'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.
'''

try:
    with open('integers.txt', 'r') as my_ints:
        data = [line.rstrip('\n') for line in my_ints]
        #print(type(data))
except IOError as e:
    print("I/O error")
except ValueError:
    print("Could not convert data to an integer.")
else:
    print(int(data[1]) * 5)

