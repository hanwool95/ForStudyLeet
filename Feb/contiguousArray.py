
# hash
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = 0
        count = 0
        count_dict = {0:[0]}
        while index != len(nums):
            if nums[index] == 0:
                count -= 1
            else:
                count += 1
            index += 1
            if count in count_dict.keys():
                count_dict[count].append(index)
            else:
                count_dict[count] = [index]
        max_sum = 0
        for key, num_list in count_dict.items():
            cur_sum = max(num_list) - min(num_list)
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


# brute
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = 0
        count_list = []
        for i in range(len(count_list)):
            count_list[i][nums[index]] += 1
        if nums[index] == 0:
            count_list.append([1, 0])
        else:
            count_list.append([0, 1])
        for zero, one in count_list:
            if (zero == one) & (zero + one > max_sum):
                max_sum = zero + one
        index += 1

        for zero, one in count_list:
            if (zero == one) & (zero + one > max_sum):
                max_sum = zero + one

        return max_sum