import inspect

class G(object):
    pass

class D(object):
    def __init__(self):
        print("D")


class E(object):
    def __init__(self):
        print("E")


class F(object):
    def __init__(self):
        print("F")


class C(D, F):
    def __init__(self):
        print("C")


class B(E, D):
    def __init__(self):
        print("B")


class A(B, C):
    def __init__(self):
        print("A")


if __name__ == '__main__':
    print(inspect.getmro(A))
