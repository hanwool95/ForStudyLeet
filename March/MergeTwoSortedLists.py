# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = None
        cur_node = None

        if not list1:
            return list2
        elif not list2:
            return list1
        elif not (list1 and list2):
            return None

        if list1.val > list2.val:
            result_node = list2
            cur_node = result_node
            list2 = list2.next
        else:
            result_node = list1
            cur_node = result_node
            list1 = list1.next

        while list1 and list2:
            if list1.val > list2.val:
                cur_node.next = list2
                cur_node = cur_node.next
                list2 = list2.next
            else:
                cur_node.next = list1
                cur_node = cur_node.next
                list1 = list1.next

        if list1:
            cur_node.next = list1
        elif list2:
            cur_node.next = list2

        return result_node