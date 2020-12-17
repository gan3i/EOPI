from test_framework import generic_test
import math


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.

    '''
    x = 313
    j = 2
    l = 3
    r = 3
    '''
    if x<=0:
        return x == 0
    # j =0
    # temp = x
    # while temp >= 10:
    #     temp = temp // 10
    #     j +=1
    num_of_digits =math.floor(math.log10(x)) +1

    msd_mask = 10 ** (num_of_digits -1)
    
    while x:
        l = x % 10
        r = x // (msd_mask)
        if l != r:
            return False
        x = (x - (msd_mask * r)) // 10

        msd_mask //=100 


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
