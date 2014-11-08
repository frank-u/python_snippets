import timeit


def checkio(n, m):
    """
    A technique for counting ones in a binary computer
    Author: 	Peter Wegner 	Massachusetts Institute of Technology, Cambridge

    Communications of the ACM CACM Homepage archive
    Volume 3 Issue 5, May 1960
    Page 322
    ACM New York, NY, USA

    http://dl.acm.org/citation.cfm?id=367236.367286
    """
    x = n ^ m
    dist = 0
    while x:
        dist += 1
        x &= x - 1
    return dist


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

    ccheckio = lambda n, m: bin(n ^ m).count("1")
    print("1: ", timeit.timeit("checkio(1117, 17)",
                               setup="from __main__ import checkio"))
    checkio = ccheckio
    print("2: ", timeit.timeit("checkio(1117, 17)",
                               setup="from __main__ import checkio"))
    #bin(111).count('5') -> fast because C code ;)