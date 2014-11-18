class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

if __name__ == '__main__':
    c1 = OneOnly()
    c1.a = 6
    c2 = OneOnly()
    print(c2.a)