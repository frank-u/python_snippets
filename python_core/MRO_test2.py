class A(object):
    def iterator(self):
        print('A.iterator')


class B(object):
    def iterator(self):
        print('B.iterator')


class C(A, B):
    def iterator(self):
        print('C.iterator')
        super(C, self).iterator()


class D(B, A):
    def iterator(self):
        print('D.iterator')
        super(D, self).iterator()


C().iterator()
print("=" * 30)
D().iterator()
