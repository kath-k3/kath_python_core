'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.
The script should keep prompting the user until they enter an integer.
'''

#import time
# while True:
#     # u_int = input("Please enter an integer: ")
#     try:
#         # type(u_int) is int
#         print("Thanks, nice integer you chose! ")
#         time.sleep(5)
#     except ValueError as valer:
#         print("Hmm, that is not an integer, please try again")


u_int = input("Please enter an integer: ")

try:
    int(u_int) == u_int
    print("Nice integer you chose!")
except ValueError as valexc:
    valexc.message = "Hmm, this is not an integer"
    print(valexc.message)


