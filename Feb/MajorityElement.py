class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sorted(counter.items(), key = lambda item: item[1], reverse=True)[0][0]