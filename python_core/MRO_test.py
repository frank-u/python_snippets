"""
    This Code Should Fail with:
    Cannot create a consistent method resolution order (MRO) for bases B, A
"""


class A:
    pass


class B(A):
    def do(self):
        print("Class B.do")


class X(A, B):
    def do(self):
        print("Class X.do")


class Y(B, A):
    def do(self):
        print("Class Y.do")


class Z(X, Y):
    def do(self):
        print("Class Z.do")


if __name__ == '__main__':
    a = Z()
    a.do()