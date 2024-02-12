# decorators_module.py

def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        return_value = f(*args, **kwargs)
        print("Ended")
        return return_value

    return wrapper


@func
def func2(x, y):
    print("i am func2")
    print(x)
    return y


@func
def func3():
    return "i am func3"


# func3 = func(func3)
# func2 = func(func2)
func3()
# func2()

x = func2(5, 6)
print(x)