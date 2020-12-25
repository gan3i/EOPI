from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.
    def sum(tree, running_sum):
        if not tree:
            return 0

        partial_sum = running_sum << 1 | tree.data
        if not tree.left and not tree.right:
            return partial_sum

        return sum(tree.left, partial_sum) + sum(tree.right, partial_sum)    

    return sum(tree,0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
