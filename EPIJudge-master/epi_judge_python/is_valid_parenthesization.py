from test_framework import generic_test
from queue import LifoQueue

def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    para_pairs = {')':'(',']':'[','}':'{'}
    stack = LifoQueue()
    for char in s:
        if char in para_pairs:
            if stack.empty() or para_pairs[char] != stack.get():
                return False
        else:
            stack.put(char)
    

    return stack.empty()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
