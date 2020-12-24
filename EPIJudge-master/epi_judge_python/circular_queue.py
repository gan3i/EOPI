from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List


class Queue:
    SIZE_FCTOR = 2
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self._values : List[int] = [0] * capacity
        self._head = self._tail = self._length = 0

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        if self._length == len(self._values):
            self._resize()
        
        self._values[self._tail] = x
        self._length += 1
        self._tail = (self._tail + 1) % len(self._values)


    def dequeue(self) -> int:
        # TODO - you fill in here.
        result :int = self._values[self._head]
        self._length -=1
        self._head = (self._head + 1) % len(self._values)
        return result

    def size(self) -> int:
        # TODO - you fill in here.
        return self._length
    
    def _resize(self) -> None:
        buffer : List[int] = [0] * (len(self._values) * Queue.SIZE_FCTOR - len(self._values))
        self._values = self._values[self._head:] + self._values[:self._head] + buffer
        self._head , self._tail = 0, self._length


# q = Queue(3)
# print(q.dequeue())

def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('circular_queue.py',
#                                        'circular_queue.tsv', queue_tester))
