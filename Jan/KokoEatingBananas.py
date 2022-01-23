class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        if len(piles) == h:
            return right
        left = 1
        while left < right:
            eat = (left + right) // 2
            count = 0
            for pile in piles:
                count += (pile // eat) + 1 if pile % eat != 0 else (pile // eat)
            if count <= h:
                right = eat
            else:
                left = eat + 1
        return right