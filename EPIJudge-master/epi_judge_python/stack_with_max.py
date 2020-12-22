from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

from typing import List

class Stack:
    my_stack = []
    MaxWithIndex = collections.namedtuple('MaxWithIndex', ('index','max'))

    def __init__(self) -> None:
        self._max_with_index : List[Stack.MaxWithIndex] = []

    def empty(self) -> bool:
        # TODO - you fill in here.
        return len(self.my_stack) == 0

    def max(self) -> int:
        # TODO - you fill in here.
        return self._max_with_index[-1].max

    def pop(self) -> int:
        # TODO - you fill in here.
        result = self.my_stack.pop()
        if len(self.my_stack) == self._max_with_index[-1].index :
            self._max_with_index.pop()
        return result


    def push(self, x: int) -> None:
        # TODO - you fill in here.
        self.my_stack.append(x)
        n = len(self.my_stack)
        if n==1:
            self._max_with_index.append(self.MaxWithIndex(n-1,x))
        elif x > self.max():
            self._max_with_index.append(self.MaxWithIndex(n-1,x))
            
        # self._max_with_index.append(self.MaxWithIndex(x,x if self.empty() else max(x, self.max())))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
