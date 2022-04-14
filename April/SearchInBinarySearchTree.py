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



# Binary Search Tree는 node값 보다 적은 값은 node의 왼쪽, 높은 값은 node의 우측에 저장하여 search하는 tree node!
# 특징 이용.

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

            if val < node.val:
                search(node.left)
            else:
                search(node.right)

        search(root)

        return self.answer

# Runtime: 79 ms, faster than 86.12% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.5 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.