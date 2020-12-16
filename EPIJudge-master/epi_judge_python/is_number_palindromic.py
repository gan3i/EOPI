from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.

    '''
    x = 313
    j = 2
    l = 3
    r = 3
    '''
    j =0
    temp = x
    while temp >= 10:
        temp = temp // 10
        j +=1

    while x:
        l = x % 10
        r = x // (10**j)
        if l != r:
            return False
        x = (x - (10 ** j * r)) // 10

        j -=2 


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
