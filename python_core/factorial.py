from datetime import datetime


class Factorial:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n - 1)
        return self.cache[n]


fact = Factorial()

if __name__ == '__main__':
    start = datetime.now()
    for i in range(10):
        print("{}! = {}".format(i, fact(i)))
    print(datetime.now() - start)
