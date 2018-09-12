#Use a "while" loop to print out every third number counting backwards from 1000 to 1.


num = 1000
count = 0

while num > 0:
    count += 1
    if count % 3 == 0:
        print (num)
    num -= 1

