'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?
'''


div_1111 = (i for i in range(1, 100000) if i%1111 == 0)

for i in div_1111:
    print(i//1111)
