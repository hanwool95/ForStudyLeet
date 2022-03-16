# Given two integer arrays pushed and popped each with distinct values,
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
# or false otherwise.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0:
            True
        cur_list = []
        pop_number = popped.pop(0)

        for number in pushed:
            cur_list.append(number)
            while pop_number == cur_list[-1]:
                cur_list.pop(-1)
                if not popped:
                    break
                pop_number = popped.pop(0)
                if not cur_list:
                    break

        return len(popped) == 0
