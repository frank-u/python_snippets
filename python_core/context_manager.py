class A():
    def __init__(self, length=0):
        self.length = length

    def __enter__(self):
        print("entered: {0}".format(self.length))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exited {0}".format(self.length))
        return True  # if everything is ok

    def __str__(self):
        return "Object state is: {0}".format(self.length)


if __name__ == '__main__':
    a = A(2)
    with a as ac:
        print(ac)