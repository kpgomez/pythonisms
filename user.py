from library import Base

assert hasattr(Base, 'foo'), "You borke it, you fool!"

class Derived(Base):
    def bar(self):
        # return self.foo()
        return 'bar'