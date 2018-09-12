#Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
#of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
#Print the results to the console.

lower_input = int(input("Please give me a number "))
higher_input = int(input("Please give me a higher number "))

print (f"The numbers you provided are {lower_input} and {higher_input}")

my_sum = higher_input
while lower_input < higher_input:
    my_sum += lower_input
    print(my_sum)
    lower_input += 1

print(f"The sum of the numbers is {my_sum}")

