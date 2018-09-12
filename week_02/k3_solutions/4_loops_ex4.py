# print out every prime number between 1 and 100

num = 2
while num <=100:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
    num += 1
