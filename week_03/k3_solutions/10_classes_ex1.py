'''
Strings methods
Demonstrate below:
- strip
- replace
- find
Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html
'''

# strip usage
string_1 = ' Guess who who   '

# Leading whitepsace are removed
print(string_1.strip())

# prints only "uess"
print(string_1.strip(' Gwho'))


# replace usage
string_2 = "this is great, this really is"

# returns 'thwas was great, thwas really was'
print(string_2.replace("is", "was"))

# returns 'thwas was great, thwas really is'
print(string_2.replace("is", "was", 3))

# find usage
string_3 = "this is string example!";
string_4 = "exam";
print(string_3.find(string_4))
print(string_3.find(string_4, 10))




