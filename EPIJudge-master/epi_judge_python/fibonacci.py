from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    if n <= 1:
        return n
    fib_minus_one, fib_minus_two = 1, 0
    for _ in range(1,n):
        fib = fib_minus_one + fib_minus_two
        fib_minus_two = fib_minus_one
        fib_minus_one = fib
    return fib_minus_one


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
