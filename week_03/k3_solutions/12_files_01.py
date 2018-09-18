'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).
Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html
'''
with open('words.txt', 'r') as f:
    data = [line.rstrip('\n') for line in f]


#print(type(data))
#print(data[:4])
for item in data:
    if len(item) >=20:
        print(item)

