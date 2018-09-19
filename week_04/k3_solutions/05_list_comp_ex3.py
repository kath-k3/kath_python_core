'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.
Tip: Use an if statement in the listcomp
'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

#for item in fish_tuple:
#    print(item)

fish_list = [item for item in fish_tuple if "fish" in item]

print(fish_list)
