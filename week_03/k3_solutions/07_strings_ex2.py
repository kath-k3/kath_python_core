#Given the two lists below, find the elements that are the same
#and put them in a new list.
#Put the elements that are different in another list.
#Print both.

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

incl_list = []
excl_list = []

#for i in list_one:
#    for j in list_two:
#        if i == j:
#            incl_list.append(i)
#        else:
#            excl_list.append(j)

#print (incl_list, excl_list)

i = 0
while i < len(list_two):
    j_index = 0
    for j in list_one:
        if list_two[i] == j:
            incl_list.append(list_two[i])
        else:
            if j_index == (len(list_one) - 1):
                excl_list.append(list_two[i])
            j_index += 1
    i += 1

print ("Inclusion list: " + str(incl_list), "Exclusion list: " + str(excl_list))
