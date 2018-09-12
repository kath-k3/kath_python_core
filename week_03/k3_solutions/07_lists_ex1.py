#Take in 10 numbers from the user. Place the numbers in a list.
#Using the loop of your choice, calculate the sum of all of the
#numbers in the list as well as the average.
#Print the results.


#number_list = [int(x) for x in input("Enter some numbers here: ").split()]

#print (number_list)
#print(len(number_list))

number_list = []
while True:
    inp = int(input("Please give me a number: "))
    number_list.append(inp)
    if len(number_list) == 10:
        break

#print (number_list)

def my_sum(given_list):
    total = 0
    for item in given_list:
        total += item
    return total


def my_ave(given_list):
    total = 0
    for item in given_list:
        total += item
    return total/len(given_list)

print(my_sum(number_list))
print(my_ave(number_list))

