'''
Write a decorator function that wraps text passed to it in <p> tags.
'''
# decorators - function that takes another function as an argument,
# generates new function, augmenting the work of the original function,
# and returning the generated function so we can use it anywhere.


def p_tagger(func):
    def func_wrapper(input_text):
        return "<p> {0}</p>".format(func(input_text))
    return func_wrapper

@p_tagger
def get_text(input_text):
    return "{0}".format(input_text)

print(get_text("Bob"))


#def p_tagger(func):
#    def func_wrapper(input_text):
#        return "<p> {0}</p>".format(func(input_text))
#    return func_wrapper

#my_get_text = p_tagger(get_text)

#print(my_get_text("Pire"))


