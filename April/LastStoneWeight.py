# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the smallest possible weight of the left stone. If there are no stones left, return 0.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            # print(stones)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
        # print(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


# Runtime: 40 ms, faster than 65.73% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 17.07% of Python3 online submissions for Last Stone Weight.


# 상위 정답자들 solution으로 python heapq 제안
# heapq: binary tree로 min heap 정렬, push 가능.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minus_list = []
        for stone in stones:
            minus_list.append(-stone)

        heapq.heapify(minus_list)

        while len(minus_list) > 1:
            print(minus_list)

            diff = abs(heapq.heappop(minus_list) - heapq.heappop(minus_list))

            if diff != 0:
                heapq.heappush(minus_list, -diff)

        if len(minus_list) == 1:
            return -minus_list[0]
        else:
            return 0


# Runtime: 34 ms, faster than 82.01% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.