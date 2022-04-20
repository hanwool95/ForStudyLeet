# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.

# First Trial

# Init할 때 Travel path를 만드는 방법으로 접.
# Init 한 뒤에 next()와 hasNext의 속도 complexity O(1), 저장 complexity O(n)
# BST 높이가 h면, Init 할 때 속도 complexity가 O(h^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur_node = root
        self.cur = 0
        self.is_root = True
        self.stack = []
        self.travel_path = []
        self.making_path()

    def next(self) -> int:
        self.cur += 1
        return self.travel_path[self.cur - 1]

    def making_path(self):

        self.going_left_side(self.cur_node)
        self.travel(self.stack.pop())

    def going_left_side(self, node):
        if node.left:
            self.stack.append(node)
            self.going_left_side(node.left)
            node.left = None
        else:
            self.stack.append(node)

    def travel(self, node):
        if node.left:
            self.going_left_side(node)
            self.travel(self.stack.pop())
        elif node.right:
            self.travel_path.append(node.val)
            self.travel(node.right)
            node.right = None
        else:
            self.travel_path.append(node.val)
            if self.stack:
                self.travel(self.stack.pop())

    def hasNext(self) -> bool:
        if self.cur >= len(self.travel_path):
            return False
        else:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Runtime: 92 ms, faster than 57.85% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 32.1 MB, less than 7.09% of Python3 online submissions for Binary Search Tree Iterator.