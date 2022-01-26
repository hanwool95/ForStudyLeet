# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def get_number(node):
            if (node.left == None) & (node.right == None):
                return [node.val]

            tree_list = [node.val]
            if node.left != None: tree_list += get_number(node.left)
            if node.right != None: tree_list += get_number(node.right)
            return tree_list

        l1 = get_number(root1) if root1 else []
        l2 = get_number(root2) if root2 else []
        result = l1 + l2
        result.sort()
        return result