# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        current1 = l1
        current2 = l2
        Flag1 = False
        Flag2 = False

        result = ListNode()
        result_target = result

        up = False

        while True:
            current_result = current1.val + current2.val
            if up:
                current_result += 1
                up = False
            if current_result > 9:
                up = True
            result_target.val = current_result % 10
            print(result_target.val)

            if current1.next == None:
                Flag1 = True
                current1.val = 0
            if current2.next == None:
                Flag2 = True
                current2.val = 0

            if Flag1 & Flag2:
                if up:
                    result_target.next = ListNode(1)
                else:
                    result_target.next = None
                return (result)
            else:
                if not Flag1:
                    current1 = current1.next
                if not Flag2:
                    current2 = current2.next
                new_result = ListNode()
                result_target.next = new_result
                result_target = new_result
