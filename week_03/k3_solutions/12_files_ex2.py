'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.
If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.
Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html
'''

# function sed
# arguments: pattern string, replacement string, two file names
# read first file into 2nd
# pattern in file -> replace with replacement
# Catch error messages, inform, exit

def sed(p_str, rep_str, file_1, file_2):
    try:
        with open(file_1, 'r') as f_1:
            try:
                with open(file_2, 'w') as f_2:
                    for line in f_1:
                        line = line.replace(p_str, rep_str)
                        f_2.write(line)
            except IOError as ioe_2:
                print(ioe_2)
    except IOError as ioe_1:
        print(ioe_1)

sed("peet", "piit", 'kapsas.txt', 'kipsas.txt')




