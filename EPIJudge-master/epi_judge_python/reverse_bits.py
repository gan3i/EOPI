from test_framework import generic_test
from swap_bits import swap_bits
from precomputed_swaps import PRECOMPUTED_SWAPS

# 6 in binary is 0b110, and its reverse in binary is 0b110000000000000000000000000000000000000000000000000000000000000

'0b110000000000000000000000000000000000000000000000000000000000000'
'0b110000000000000000000000000000000000000000000000000000000000000'
# print(3<<64)

def reverse(x):
    result = 0
    for i in range(64):
        result <<= 1
        result |= x & 1
        x >>= 1

    return result

# print(reverse(1351510410656))

def precompute_swap():
    precomputed_swap = [0 for _ in range(2**16)]
    y = 0
    
    while y < 2 ** 16:
        #result = 0
        # temp = y
        # while temp:
        #     result <<= 1
        #     result |= temp & 1
        #     temp >>= 1

        precomputed_swap[y] = reverse(y)

        y +=1


    file = open('precomputed_swaps.txt','wt')
    file.write('[' + ','.join(str(x) for x in precomputed_swap) + ']')

# print(PRECOMPUTED_SWAPS[65535])



# precompute_swap()

def reverse_bits(x: int) -> int:
    # TODO - you fill in here.

    return reverse(x)


    bit_mask = 0xFFFF
    mask_size = 16
    x1=PRECOMPUTED_SWAPS[x & bit_mask] #<< (3* mask_size)
    x2=PRECOMPUTED_SWAPS[(x>>mask_size) & bit_mask] #<< (2 * mask_size)
    x3=PRECOMPUTED_SWAPS[(x>>(2*mask_size)) & bit_mask] #<< (mask_size)
    x4=PRECOMPUTED_SWAPS[(x>>(3*mask_size)) & bit_mask]
    return   (x1 | x2 | x3 | x4)
            

# print(reverse_bits(1351510410656))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))