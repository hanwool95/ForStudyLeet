# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        cur_node = head
        if head == None:
            return None
        while cur_node.next != None:
            if cur_node in node_set:
                return cur_node
            node_set.add(cur_node)
            cur_node = cur_node.next
        return None

