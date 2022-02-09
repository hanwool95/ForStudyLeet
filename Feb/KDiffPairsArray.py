class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        rslt_lst = []
        for i in range(len(nums)):
            num = nums.pop(0)
            if (num + k in nums) & (num not in rslt_lst):
                rslt_lst.append(num)
            nums.append(num)

        return len(rslt_lst)

