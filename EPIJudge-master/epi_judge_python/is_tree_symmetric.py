from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def check_symmetry(subtree_1, subtree_2):
        if not subtree_1 and not subtree_2:
            return True
        if subtree_1 and subtree_2:
            return (subtree_1.data == subtree_2.data 
                    and check_symmetry(subtree_1.left, subtree_2.right) 
                    and check_symmetry(subtree_2.left, subtree_1.right))
        return False
    if not tree:
        return True
    else:
        return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
