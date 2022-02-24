# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_dict = {}
        cur_node = head
        if not head:
            return None
        while True:
            if cur_node.next == None:
                if cur_node.val in val_dict.keys():
                    val_dict[cur_node.val].append(cur_node)
                else:
                    val_dict[cur_node.val] = [cur_node]
                break
            else:
                save_node = cur_node
                cur_node = cur_node.next
                save_node.next = None
                if save_node.val in val_dict.keys():
                    val_dict[save_node.val].append(save_node)
                else:
                    val_dict[save_node.val] = [save_node]

        sorted_list = sorted(val_dict.items(), key = lambda item: item[0])

        for i in range(len(sorted_list)-1):
            if len(sorted_list[i][1]) > 1:
                for j in range(len(sorted_list[i][1])-1):
                    sorted_list[i][1][j].next = sorted_list[i][1][j+1]
                sorted_list[i][1][len(sorted_list[i][1])-1].next = sorted_list[i+1][1][0]
            else:
                sorted_list[i][1][0].next = sorted_list[i+1][1][0]

        return sorted_list[0][1][0]