class Solution:
    @lru_cache(maxsize=None)
    def is_win(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True

        for i in range(math.floor(math.sqrt(n))):
            cur = n -(i+1)**2
            if not self.is_win(cur):
                return True

    def winnerSquareGame(self, n: int) -> bool:
        return self.is_win(n)