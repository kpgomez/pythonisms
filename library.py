
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        return super().__new__(cls, name, bases, body)

    def __init_subclass__(cls, **kwargs):
        return super().__init_subclass__()

class Base(metaclass=BaseMeta):
            def foo(self):
                # return 'foo'
                return self.bar


for _ in range(10):
    class Base: pass


class Base:
    for _ in range(10):
        def bar(self):
            pass


def _():
    class Base:
        pass


from dis import dis
dis(_)

old_bc = __build_class__


def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)


import builtins
builtins.__build_class__ = my_bc