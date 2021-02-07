from test_framework import generic_test
import functools

def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def compute_distance_between_prefixes(a_idx, b_idx):
        if a_idx < 0:
            return b_idx + 1
        elif b_idx < 0:
            return a_idx + 1
        
        if A[a_idx] == B[b_idx]:
            return compute_distance_between_prefixes(a_idx - 1, b_idx -1)

        sub_last = compute_distance_between_prefixes(a_idx - 1, b_idx -1)
        add_last = compute_distance_between_prefixes(a_idx, b_idx -1)
        del_last = compute_distance_between_prefixes(a_idx - 1, b_idx)

        # if sub_last and add_last and del_last:
        #     print("hello")

        return 1 + min(sub_last, add_last, del_last)
    
    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
