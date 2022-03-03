class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        cur_count = 0

        sub_seq = None
        prev_num = nums.pop(0)

        for number in nums:
            if number - prev_num != sub_seq:
                if cur_count > 1:
                    for i in range(cur_count - 1):
                        count += i + 1
                cur_count = 0
                sub_seq = number - prev_num

            prev_num = number
            cur_count += 1

        if cur_count > 1:
            for i in range(cur_count - 1):
                count += i + 1
        return count
