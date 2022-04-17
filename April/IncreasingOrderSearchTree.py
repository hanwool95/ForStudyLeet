# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result_node = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.result_node = root

        def find_node(node, target=None):
            if node.val < self.result_node.val:
                self.result_node = node

            if (not node.left) and (not node.right):
                if target:
                    node.right = target
                return node

            else:
                left_node = node.left
                node.left = None
                right_node = node.right
                node.right = None

                if left_node:
                    left_head = find_node(left_node, node)

                if right_node:
                    right_head = find_node(right_node, target)
                    node.right = right_head
                else:
                    node.right = target

                if left_node:
                    return left_head
                else:
                    return node

        find_node(root)
        return self.result_node


# Runtime: 37 ms, faster than 70.10% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 14.1 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.

# recursive 함수 작성하는 방법으로 접근.
# base case는 childeren이 모두 없을 때 target을 right child로 두는 것으로 결정.
# root는 값들을 조회해서 가장 작은 값으로 설정
# recursive한 방법으로 조회를 하기에 모든 값을 한 번씩 방문하여 프로그램 반복. -> Runtime complexity O(n)