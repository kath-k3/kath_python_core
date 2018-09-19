num_list = [1, 2, 3, 4]

new_lit = [item**2
            for item in num_list
            if item%2 == 0]



# generator
gen = (n**2 for n in num_list)
print(type(gen))
for n in gen:
    print(n)
