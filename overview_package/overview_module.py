# overview_module.py

# example one
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog


# example two
def inner_function(num):
    for i in range(num):
        def show():
            print(i*2)

        show()


# example three
def func(x):
    if x == 1:
        def return_value():
            return "x is equal to 1"
    else:
        def return_value():
            return "x is not 1"

    return return_value

