import inspect
from queue import Queue


# example one
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog


# example two
for i in range(10):
    def show():
        print(i*2)

    show()


# example three
def func(x):
    if x == 1:
        def return_value():
            print("x is equal to 1")
    else:
        def return_value():
            print("x is not 1")

    return return_value


# example one, make_class
cls = make_class(10)
d = cls("Tim")
print(d.name)
d.print_value()


# example three, func
new_func = func(2)
new_func()
another_func = func(1)
another_func()

# inspect functions
print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))

# show source code
print(inspect.getsource(Queue))