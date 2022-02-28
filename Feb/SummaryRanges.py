class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result

        start = nums.pop(0)
        count = 1

        for number in nums:
            if start + count != number:
                if count == 1:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(start + count - 1))

                start = number
                count = 1
            else:
                count += 1
        if count == 1:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(start + count - 1))

        return result