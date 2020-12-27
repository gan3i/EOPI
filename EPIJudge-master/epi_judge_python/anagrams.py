from typing import List
import collections
from typing import List, DefaultDict

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # TODO - you fill in here.
    anagram_groups : DefaultDict[str,List[str]] = collections.defaultdict(list) 

    for s in dictionary:
        anagram_groups[''.join(sorted(s))].append(s)

    return [group for group in anagram_groups.values() if len(group) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
