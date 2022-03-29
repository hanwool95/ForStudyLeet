# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n_dict = Counter(nums)
        sorted_dict = sorted(n_dict.items(), key = lambda x: x[1], reverse=True)
        for key, value in sorted_dict:
            return key

# Runtime: 706 ms, faster than 77.38% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 30.2 MB, less than 22.19% of Python3 online submissions for Find the Duplicate Number.