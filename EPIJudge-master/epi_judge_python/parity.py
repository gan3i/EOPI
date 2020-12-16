from test_framework import generic_test
from typing import List
from precomputed_parity import PRECOMPUTED_PARITY

#without cache, by errasing the least set bit everytime O(k) where k is the number of the set bit
# def parity(x : int) ->int:

#     result = 0 
#     while x:
#         result ^=1
#         x &=x-1
#     return result


#precompute the parity of all first 2** 16 integers
# def precompute(precomputed_parity: List[int]) -> None:

#     y = 0
#     while y < 2 ** 16:
#         precomputed_parity[y] = parity(y)
#         y += 1
#     file = open("precomputed_parity.txt","wt")
#     file.write('[' + ','.join(str(x) for x in precomputed_parity) + ']')



# #Compute the parity by using the precomputed parity, bit masking and bit fiddling O(word size/ mask_size)
# def parity(x: int) -> int:
#     # TODO - you fill in here.
#     # precomputed_parity = [0 for _ in range((2**16))]
#     # precompute(precomputed_parity)

#     mask_size = 16
#     bit_mask = 2 ** 16 - 1 # or 0xFFFF

#     return PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^ \
#     PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^ \
#     PRECOMPUTED_PARITY[(x >> (mask_size)) & bit_mask] ^ \
#     PRECOMPUTED_PARITY[x & bit_mask]

#using Comutative nature of XOR O(logn)
def parity(x : int) ->int:
    x ^= x >> 32
    x ^= x >> 16
    return PRECOMPUTED_PARITY[x & 2 ** 16 -1]
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 0x1
# print(parity(14))



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
