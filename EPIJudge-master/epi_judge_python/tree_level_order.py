from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    result : List[List[int]] = []
    if not tree:
        return result

    current_depth_nodes = [tree]

    while current_depth_nodes:
        result.append([node.data for node in current_depth_nodes if node])

        current_depth_nodes = [child for curr in current_depth_nodes for child in (curr.left, 
                            curr.right) if child]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
