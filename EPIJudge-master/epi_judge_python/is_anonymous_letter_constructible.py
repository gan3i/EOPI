from test_framework import generic_test
from typing import Dict


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.

    char_count : Dict[chr,int] ={} 

    for c in magazine_text:
        if c in char_count:
            char_count[c] +=1
        else:
            char_count[c] =1

    for c in letter_text:
        if c not in char_count:
            return False
        elif char_count[c] == 0:
            return False
        char_count[c] -= 1

    # for value in char_count.values():
    #     if value > 0:
    #         return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
