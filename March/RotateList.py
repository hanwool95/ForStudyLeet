# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        cur_node = head
        index_dict = {}
        count = 0
        while True:
            index_dict[count] = cur_node
            if not cur_node.next:
                break
            cur_node = cur_node.next
            count += 1
        if count + 1 == k:
            return head
        target = k % (count + 1)
        if target == 0:
            return head
        index_dict[count - target].next = None
        index_dict[count].next = head

        return index_dict[count - target + 1]



