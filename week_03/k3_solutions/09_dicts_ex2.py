'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.
'''

dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

# Python 3 has merge feature for dicts.

def merge_dicts(dict1, dict2):
    '''Merges 2 dictionaries while leaving the initial dictionaries intact '''

    m_dict = dict1.copy()   # start with dict1 keys and values
    m_dict.update(dict2)    # modifies merged_dict with dict2's keys and values & returns None
    return m_dict

one_two = merge_dicts(dict_1, dict_2)
final_merged = merge_dicts(one_two, dict_3)
print(final_merged)

for key, value in final_merged.items():
    print(key, value)
