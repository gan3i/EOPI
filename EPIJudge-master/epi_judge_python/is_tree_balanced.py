from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    BalancedStatuswithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree :BinaryTreeNode) ->bool:
        if not tree: 
            return BalancedStatuswithHeight(True,-1)
        else:
            left = check_balanced(tree.left)
            if not left.balanced:
                return left
            right = check_balanced(tree.right)
            if not right.balanced:
                return right

            if abs(right.height - left.height) > 1:
                return BalancedStatuswithHeight(False,0)
            
            return BalancedStatuswithHeight(True,max(left.height, right.height) + 1)

    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
