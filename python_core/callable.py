class Joe:
    def __init__(self, age):
        self.age = age


if __name__ == '__main__':
    joe = Joe(15)
    print("Joe:", joe.age)
    cjoe = Joe.__call__(56)
    print(cjoe.age)
    print("is class callable?", callable(Joe))
    print("is  obj  callable?", callable(joe))