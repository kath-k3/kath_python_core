

#try:
#    my_list = [1, 2]
#    print


def divide(arg1, arg2):
    try:
        return_value = arg1/arg2
    except ZeroDivisionError as exc:
        raise exc
    else:
        return return_value

try:
    print(divide(10, 0))
except ZeroDivisionError as zde:
    print(zde)


class MyException(Exception):

    status_codes = {404: "not found", 500: "server error"}

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        self.status_message = MyException.status_codes[status_code]

    def __str__(self):
        return "Nw way to print"


x = 10
y = 0

try:
    if (y == 0):
        raise MyException(404, "exception raised")
    print(x/y)
except MyException as exc:
    print("error with status code: ", exc.status_code)
    print("with message: ", exc.message)
