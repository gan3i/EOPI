import collections

from queue import LifoQueue
from typing import List

from test_framework import generic_test, test_utils


mnemonic = collections.namedtuple("Mnemonic",('count','running_mnemonic'))

mapping = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
def phone_mnemonic(phone_number: str) -> List[str]:
    first = mnemonic(0,'')
    stack = LifoQueue()
    stack.put(first)
    result = []

    while not stack.empty():
        curr = stack.get()
        if curr.count == len(phone_number):
            result.append(curr.running_mnemonic)
        else:
            for char in mapping[int(phone_number[curr.count])]:
                stack.put(mnemonic(curr.count + 1, curr.running_mnemonic +char))
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
