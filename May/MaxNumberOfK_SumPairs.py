class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0

        counter = Counter(nums)

        for num in counter.keys():
            if num < k:
                diff = abs(k - num)
                if diff in counter.keys():
                    min_count = min(counter[num], counter[diff])
                    if num != diff:
                        count += min_count
                        counter[num] -= min_count
                        counter[diff] -= min_count
                    else:
                        if min_count > 1:
                            div_2 = min_count // 2
                            count += div_2
                            counter[num] -= div_2
        return count

# Runtime: 875 ms, faster than 47.32% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.1 MB, less than 33.48% of Python3 online submissions for Max Number of K-Sum Pairs.

