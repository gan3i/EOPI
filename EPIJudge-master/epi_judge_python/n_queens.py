from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    def solve_n_queens(row):
        if row == n:
            result.append(col_placement.copy())
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row -  i) 
            for i, c in enumerate(col_placement[:row])):
                col_placement.append(col)
                solve_n_queens(row + 1)
                col_placement.pop()
    result = []
    col_placement = []
    solve_n_queens(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
