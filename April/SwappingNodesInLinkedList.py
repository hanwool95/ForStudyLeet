# You are given the head of a linked list, and an integer k.
#
# Return the head of the linked list after swapping the values of the kth node
#
# from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head.next == None:
            return head

        head_list = [head]
        tail_list = []
        swap_node_list = []

        cur_node = head
        prev_node = None
        index = 1

        first_index = None

        head_change = False
        if k == 1:
            head_change = True

        while cur_node:
            # print(index)
            if index == k:
                if prev_node:
                    prev_node.next = None
                    tail_list.append(prev_node)

                swap_node_list.append(cur_node)
                prev_node = cur_node
                cur_node = cur_node.next
                prev_node.next = None

                head_list.append(cur_node)

                if not first_index:
                    first_index = index
            else:
                prev_node = cur_node
                cur_node = cur_node.next
            index += 1

            if cur_node == None and len(swap_node_list) < 2:

                # print(swap_node_list)
                # print(head_list)
                # print(tail_list)
                # print(index)
                # print(k)

                if k == index - k:
                    tail_list[0].next = swap_node_list[0]
                    swap_node_list[0].next = head_list[1]
                    return head

                if index == 3 and k == 2:
                    swap_node_list[0].next = head_list[0]
                    return swap_node_list[0]

                if index - k == 1:
                    swap_node_list[0].next = head_list[0].next
                    head_list[0].next = None
                    tail_list[0].next = head_list[0]
                    return swap_node_list[0]

                k = index - k
                # print(k)
                if k > (index - 1) / 2:
                    cur_node = head_list[1]
                    index = first_index + 1
                else:
                    # print(swap_node_list)
                    # print(head_list)
                    # print(tail_list)
                    cur_node = head_list[0]
                    index = 1
                prev_node = None

        # print(swap_node_list)
        # print(head_list)
        # print(tail_list)

        if len(tail_list) == 2:
            if swap_node_list[1] != tail_list[0]:
                tail_list[0].next = swap_node_list[1]
                swap_node_list[1].next = head_list[1]
                tail_list[1].next = swap_node_list[0]
                swap_node_list[0].next = head_list[2]
            else:
                tail_list[1].next = swap_node_list[0]
                swap_node_list[0].next = swap_node_list[1]
                swap_node_list[1].next = head_list[1]
        elif len(tail_list) == 1:
            if head_change:
                tail_list[0].next = swap_node_list[0]
                swap_node_list[1].next = head_list[1]
                head = swap_node_list[1]
            else:
                tail_list[0].next = swap_node_list[1]
                swap_node_list[1].next = swap_node_list[0]
                swap_node_list[0].next = head_list[2]
        else:
            head_list[1].next = head_list[0]
            head_list[0].next = None
            if head_change:
                head = head_list[1]

        return head


# Runtime: 1176 ms, faster than 74.25% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.6 MB, less than 31.04% of Python3 online submissions for Swapping Nodes in a Linked List.