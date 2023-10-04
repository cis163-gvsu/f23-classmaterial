class Top(object):
    def __init__(self):
        print('beginning top level')
        super().__init__()
        print('exiting top level')

class MiddleA(Top):
    def __init__(self):
        print('beginning middle A')
        super().__init__()
        print('exiting middle A')

    def moo(self):
        print('moo A')


class MiddleB(Top):
    def __init__(self):
        print('beginning middle B')
        super().__init__()
        print('exiting middle B')

    def moo(self):
        print('moo B')


class Bot(MiddleA, MiddleB):
    def __init__(self):
        print('beginning bottom')
        super().__init__()
        print('exiting bottom')

    def my_moo(self):
        print('bot moo')
        #super().moo() # calls first parent of bot in MRO
        #super(MiddleA, self).moo() #goes based on what comes after MiddleA in MRO
        super(Bot.__mro__[1], self).moo()


b = Bot()
print(Bot.__mro__)
b.my_moo()
