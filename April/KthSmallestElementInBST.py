# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# First trial

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order_list = [root.val]

        def put_node_in_list(node):
            if node.left:
                order_list.insert(order_list.index(node.val), node.left.val)
                put_node_in_list(node.left)
            if node.right:
                order_list.insert(order_list.index(node.val) + 1, node.right.val)
                put_node_in_list(node.right)

        put_node_in_list(root)

        return order_list[k - 1]

# Runtime: 1064 ms, faster than 5.34% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 48.12% of Python3 online submissions for Kth Smallest Element in a BST.

# recursive 한 method로 value가 순서대로 포함된 list로 decoding한 뒤 k - 1 index를 찾아가는 방법을 사용해 봄.
# 길이가 길어질수록 사이마다 list에 insert할 때 index를 조회하기에 runtime이 O(n^2)임.
# O(n)으로 만들기 위해서는 BST를 decoding하는 과정에서 역으로 순서를 조회해야 함.
# 역으로 node를 올라가기 위해서는 모든 left node를 조회하여 데이터를 쌓아야 하는데, FILO 형식의 stack 규칙을 따르기로 결정.
# 모든 left에 대해서 stack으로 쌓아 놓고 없으면 stack pop 한 뒤 right 조회하는 방향으로 결정.



# Second Trial

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_stack = []

        def put_node_in_stack(node):
            node_stack.append(node)
            if node.left:
                put_node_in_stack(node.left)
                node.left = None

        def decoding_node(count):
            cur_node = node_stack.pop()
            if count == k:
                return cur_node.val
            else:
                if cur_node.right:
                    put_node_in_stack(cur_node.right)
                return decoding_node(count + 1)

        put_node_in_stack(root)

        return decoding_node(1)

# Runtime: 52 ms, faster than 89.88% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 16.7 MB, less than 99.72% of Python3 online submissions for Kth Smallest Element in a BST.

# O(n)으로 줄이면서 런타임 상위 90%, stack 구조로 저장 공간 최적화해서 메모리 상위 99% 달성.