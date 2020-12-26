from typing import List

from test_framework import generic_test
from heapq import heappush, heapify, heappop,merge


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
  
    #pythonic solution
    #return list(merge(*sorted_arrays)

    #try it later by creating iterator to each array in the sorted_array

    result = []
    min_heap  = []
    sorted_arr_iters =[iter(x) for x in sorted_arrays]

    for index, itr in enumerate(sorted_arr_iters):
        first_element = next(itr,None)
        if first_element is not None:
            min_heap.append((first_element,index))

    heapify(min_heap)

    while min_heap:
        smallest,kth_index = heappop(min_heap)
        result.append(smallest)

        next_entry = next(sorted_arr_iters[kth_index],None)

        if next_entry is not None:
            heappush(min_heap,(next_entry,kth_index))

    return result

    #k = len(sorted_arrays)
    # min_heap = []
    # for index in range(k):
    #     if len(sorted_arrays[index]) > 0:
    #         min_heap.append((sorted_arrays[index][0],index,0))

    # heapify(min_heap)

    # while min_heap:
    #     min_value,kth_index, index = heappop(min_heap)
    #     result.append(min_value)

    #     if (index) <= len(sorted_arrays[kth_index])-2:
    #         heappush(min_heap,(sorted_arrays[kth_index][index+1],kth_index,index+1))
            

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
