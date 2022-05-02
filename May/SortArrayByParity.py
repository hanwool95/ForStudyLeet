# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        return even + odd

# Runtime: 91 ms, faster than 67.73% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 17.91% of Python3 online submissions for Sort Array By Parity.



class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new_list = []
        for num in nums:
            if num % 2:
                new_list.append(num)
            else:
                new_list.insert(0, num)
        return new_list


# Runtime: 97 ms, faster than 59.27% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.5 MB, less than 96.65% of Python3 online submissions for Sort Array By Parity.