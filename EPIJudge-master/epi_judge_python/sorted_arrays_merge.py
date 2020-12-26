from typing import List

from test_framework import generic_test
from heapq import heappush, heapify, heappop


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.

    k = len(sorted_arrays)
    result = []
    min_heap = []
    for index in range(k):
        if len(sorted_arrays[index]) > 0:
            min_heap.append((sorted_arrays[index][0],index,0))

    heapify(min_heap)

    while min_heap:
        min_value,kth_index, index = heappop(min_heap)
        result.append(min_value)

        if (index) <= len(sorted_arrays[kth_index])-2:
            heappush(min_heap,(sorted_arrays[kth_index][index+1],kth_index,index+1))
            

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
