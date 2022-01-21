class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index = 0
        cur_i = 0

        n = len(gas)

        if (sum(gas) < sum(cost)):
            return -1

        cur_gas = 0
        while index != n:
            cur_gas += gas[index]
            cur_gas -= cost[index]
            if cur_gas < 0:
                cur_i = index + 1
                cur_gas = 0
            index += 1
        return cur_i