from typing import List

from test_framework import generic_test, test_utils


mapping = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
def phone_mnemonic(phone_number: str) -> List[str]:
    return phone_mnemonic_helper([], phone_number, 0, ['0']*len(phone_number))

def phone_mnemonic_helper(result, phone_number, count, running_mnemonic):
    if count == len(phone_number):
        result.append(''.join(running_mnemonic))
    else:
        for char in mapping[int(phone_number[count])]:
            running_mnemonic[count] = char
            phone_mnemonic_helper(result, phone_number, count + 1, running_mnemonic)
            # num_string.pop()
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
