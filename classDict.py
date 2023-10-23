class Sample:
    __test = {}

    def __init__(self):
        self.__dict__ = self.__test
        self.key = "answer"
        self.count = "numbers"

    def print_test(self):
        print(self.__test)


s = Sample()

s.print_test()