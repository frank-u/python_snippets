from unittest import TestCase


# Implemented PQ using binary heap in a list ;)
class PriorityQueue():
    def __init__(self):
        # queue - is a binary heap in a list
        self.__queue = []

    def push(self, value):
        self.__queue.append(value)
        self.__swim(len(self.__queue) - 1)

    def pop(self):
        if len(self.__queue) == 1:
            return self.__queue.pop()
        last = self.__queue.pop()
        res = self.__queue[0]
        self.__queue[0] = last
        self.__sink(0)
        return res

    def is_empty(self):
        if len(self.__queue) > 0:
            return False
        else:
            return True

    def __less(self, k1, k2):
        return self.__queue[k1] < self.__queue[k2]

    def __swap(self, k1, k2):
        self.__queue[k1], self.__queue[k2] = self.__queue[k2], self.__queue[k1]

    def __swim(self, k):
        virtual_index = k + 1
        while (virtual_index > 1) and (
                self.__less(virtual_index // 2 - 1, virtual_index - 1)):
            self.__swap(virtual_index // 2 - 1, virtual_index - 1)
            virtual_index //= 2

    def __sink(self, k):
        virtual_index = k + 1
        while (virtual_index * 2) <= len(self.__queue):
            child = 2 * virtual_index
            if (child < len(self.__queue)) and (
                    self.__less(child - 1, child)):
                child += 1
            if self.__less(virtual_index - 1, child - 1):
                self.__swap(virtual_index - 1, child - 1)
            virtual_index = child

    def __repr__(self):
        return "Priority queue: {0}.".format(self.__queue)


class PriorityQueueTests(TestCase):
    def test_isempty(self):
        pq = PriorityQueue()
        self.assertEqual(pq.is_empty(), True)

    def test_swim(self):
        data = [0, 1, 2, 3, 4]
        pq = PriorityQueue()
        for item in data:
            pq.push(item)
        self.assertEqual(pq._PriorityQueue__queue, [4, 3, 1, 0, 2])

    def test_sink(self):
        pq = PriorityQueue()
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        for item in data:
            pq.push(item)
        pq.pop()
        self.assertEqual(pq._PriorityQueue__queue, [8, 7, 4, 6, 5, 2, 3, 1, 0])

    def test_sink2(self):
        pq = PriorityQueue()
        data = [0, 1, 2, 3, 4]
        for item in data:
            pq.push(item)
        pq.pop()
        self.assertEqual(pq._PriorityQueue__queue, [3, 2, 1, 0])

    def test_pq1(self):
        pq = PriorityQueue()
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        for item in data:
            pq.push(item)
        sorted_list = []
        while not pq.is_empty():
            res = pq.pop()
            sorted_list.append(res)
        self.assertEqual(sorted_list,
                         [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                         msg="Wrong result")


if __name__ == '__main__':
    q = PriorityQueue()
    print(q)
