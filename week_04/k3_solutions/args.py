def my_function(x, y, z, *args):
    sum = 0
    for i in args:
        sum += i
    print sum


def my_kwargs_function(**kwargs): #key word arguments; dictionary
    for key, value in kwargs.items():
        print(key, value)

my_kwargs_function(x=1, y=2)
