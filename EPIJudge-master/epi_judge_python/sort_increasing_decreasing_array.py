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

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    sub_arrays : List[List[int]] = []
    start_index = 0
    incr, dcr = 1,2 
    running_type = incr

    for i in range(1,len(A)):

        if A[i-1] < A[i] and running_type == dcr:
            sub_arrays.append(A[i-1:start_index-1:-1])
            running_type = incr
            start_index = i
        elif A[i-1] > A[i] and running_type == incr:
            sub_arrays.append(A[start_index : i])
            running_type = dcr
            start_index = i

    if running_type == incr:
        sub_arrays.append(A[start_index : i+1])
    else:
        sub_arrays.append(A[i:start_index-1:-1])

    return merge_sorted_arrays(sub_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
