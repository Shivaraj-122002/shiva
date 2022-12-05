class Add:
    @staticmethod
    def add(a,b):
        print(a+b)
class Sub:
    @staticmethod
    def sub(a,b):
        print(a-b)

class Div:
    @staticmethod
    def div(a,b):
        print(a/b)


class calc(Add,Sub,Div):
    pass
calc.add(1,5)
