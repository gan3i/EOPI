from binary_tree_node import BinaryTreeNode
from test_framework import generic_test




def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    def is_bst(root: BinaryTreeNode, max_val: int, min_val:int) ->bool:
        if not root:
            return True
        if root.data > max_val or root.data < min_val: # this condition should be clarified
            return False
        return is_bst(root.left, root.data, min_val) and is_bst(root.right, max_val, root.data)
        

    return is_bst(tree,float("inf"),float("-inf"))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
