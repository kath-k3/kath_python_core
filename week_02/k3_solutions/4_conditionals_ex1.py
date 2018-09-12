#collect input from the user
user_input = int(input("Enter a number between 1 and 1,000,000,000 \
to see whether is it odd or even: "))

#print the number the user inputed to the console
print(f"The user input is {user_input}")

#complete the rest of the code to determine whether it is odd or even
if user_input % 2 == 0:
    print(f"{user_input} is EVEN")
else:
    print(f"{user_input} is ODD")


#A formatted string literal or f-string is a string literal
#that is prefixed with 'f' or 'F'. These strings may contain replacement fields,
#which are expressions delimited by curly braces {}.
#While other string literals always have a constant value,
#formatted strings are really expressions evaluated at run time.
