import types


class Strategy():
    def __init__(self, function=None):
        self.name = "Default Function"

        if function is not None:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("Executing Default strategy")


def strategy_one(self):
    print("Executing {}".format(self.name))


def strategy_two(self):
    print("Executing {}".format(self.name))


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
