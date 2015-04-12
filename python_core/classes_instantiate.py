class A(object):
    def __new__(cls):
        obj = super(A, cls).__new__(cls)
        print("created object\t{0}".format(obj))
        return obj

    def __init__(self):
        print("init object\t{0}".format(self))


if __name__ == '__main__':
    ca = A()

