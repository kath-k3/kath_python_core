'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.
The provided code to start is in file Point1.py in this folder.
'''

# Not sure what we have to do here..

import math
import classes_point1

def line_between_points(p1, p2):
    x_dist = p2.x - p1.x
    y_dist = p2.y - p1.y
    # math.hypot(x, y) -
    # return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y)
    line_length = round(math.hypot(x_dist, y_dist), 1)
    print(line_length)


my_p_1 = classes_point1.Point()
my_p_1.x = 20.0
my_p_1.y = 50.0

my_p_2 = classes_point1.Point()
my_p_2.x = 10.0
my_p_2.y = 10.0

classes_point1.print_point(my_p_1)
classes_point1.print_point(my_p_2)
line_between_points(my_p_1, my_p_2)
