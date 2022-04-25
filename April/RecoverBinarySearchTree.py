# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def put_list_in_result(node_list, index, result):

            if result[index]:
                result[index] = [result[index][0], node_list[1]]
            else:
                result[index] = node_list

        def discover_Tree(node, target_left=None, target_right=None):
            result = [[], []]

            if target_left:
                if target_left.val < node.val:
                    put_list_in_result([target_left, node], 0, result)
            if target_right:
                if target_right.val > node.val:
                    put_list_in_result([target_right, node], 1, result)

            if node.left:
                left, right = discover_Tree(node.left, node, target_right)
                if left:
                    put_list_in_result(left, 0, result)
                if right:
                    put_list_in_result(right, 1, result)
            if node.right:
                left, right = discover_Tree(node.right, target_left, node)
                if left:
                    put_list_in_result(left, 0, result)
                if right:
                    put_list_in_result(right, 1, result)

            return result

        def change_node(origin, changed):
            saved_val = origin.val
            origin.val = changed.val
            changed.val = saved_val

        left, right = discover_Tree(root)

        if left and right:
            if left[0] == right[0]:
                change_node(left[1], right[1])
            else:
                change_node(left[0], right[0])
        elif left:
            change_node(left[0], left[1])
        else:
            change_node(right[0], right[1])


# wrong answer in input
# [146,71,-13,55,null,231,399,321,null,null,null,null,null,-33]

# pass case
# [3,null,2,null,1]
# [1,3,null,null,2]
# [2,3,1]
# [3,1,4,null,null,2]