# data_model.py
from queue import Queue as q


# example one
class Person:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Dog({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument")

        self.name = self.name * x

    def __call__(self, y):
        print(y)


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Cat({self.name})"

    def __len__(self):
        return len(self.name)


class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()


# example one
person = Person("tim")
print(person)  # shows memory address

dog = Dog("georgina")
print("before * shows", dog)  # shows Dog(georgina)

dog * 4
print("after * shows", dog) # shows Dog(georginageorginageorginageorgina)

dog(4) # shows 4

cat = Cat("reese")
print(cat) # shows Dat(reese)
print(len(cat))

# example two
queue = Queue()
print(queue)
queue + 9
print(queue)
queue + 3
print(queue)
queue - None
print(queue)