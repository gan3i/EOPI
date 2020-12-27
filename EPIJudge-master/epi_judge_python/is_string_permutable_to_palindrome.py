from test_framework import generic_test
from typing import DefaultDict
import collections


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    char_count : DefaultDict[chr,int] = collections.defaultdict(int)

    for c in s:
        char_count[c] += 1

    is_even_len = True if len(s) % 2 == 0 else False
    odd_count = 0
    
    for value in char_count.values():

        odd_count += value % 2

        if is_even_len and odd_count > 0:
            return False

        if not is_even_len and odd_count > 1:
            return False
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
