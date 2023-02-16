# Multiple Inheritances : classes that inherit from multiple class

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)  # method resolution order, that's why we saw class A


c = C()
c.showprops()
print(C.__mro__)  # to print the method resolution order
# This is why we don't use multiple inheritance often
