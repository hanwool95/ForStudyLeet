# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    Flag = False
    answer = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):
            if self.Flag:
                return None

            if not node:
                return None

            elif node.val == val:
                self.Flag = True
                self.answer = node
                return None


            search(node.left)
            search(node.right)

        search(root)

        return self.answer


# Runtime: 84 ms, faster than 78.42% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.6 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.