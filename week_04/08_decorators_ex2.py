'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.
'''

def tags(tag_name):
    def p_tagger(func):
        def func_wrapper(input_text):
            return "<{0}>{1}</{0}>".format(tag_name, func(input_text))
        return func_wrapper
    return p_tagger

@tags("p")
def get_text(input_text):
    return input_text

print(get_text("Bob"))
