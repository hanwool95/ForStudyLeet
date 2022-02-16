# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        result_node = head
        is_result = True
        prev_node = None
        while cur_node != None and cur_node.next != None:
            if is_result:
                result_node = cur_node.next
                is_result = False
            next_node = cur_node.next
            cur_node.next = next_node.next
            next_node.next = cur_node
            if prev_node:
                prev_node.next = next_node
            prev_node = cur_node
            cur_node = cur_node.next

        return result_node