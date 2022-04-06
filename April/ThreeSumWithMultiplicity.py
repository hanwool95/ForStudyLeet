# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
#
# As the answer can be very large, return it modulo 109 + 7.

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        def answer(digit):
            return digit % (10 ** 9 + 7)

        count_num = Counter(arr)
        # print(count_num)

        result = 0

        cal_list = []

        for i, fir_num in enumerate(count_num.keys()):

            if target - fir_num * 2 == fir_num and fir_num not in cal_list:
                print("!")
                result += (count_num[fir_num]) * (count_num[fir_num] - 1) * (count_num[fir_num] - 2) / 6
                print(count_num[fir_num])
                cal_list.append(fir_num)

            for sec_num in list(count_num.keys())[i + 1:]:
                target_num = target - fir_num - sec_num

                num_list = sorted([fir_num, sec_num, target_num])
                # print(num_list)
                if target_num in count_num.keys() and num_list not in cal_list:
                    num_set = set(num_list)

                    if len(num_set) == 3:
                        result += count_num[fir_num] * count_num[sec_num] * count_num[target_num]

                    if len(num_set) == 2:
                        if num_list[0] in num_list[1:]:

                            result += (count_num[num_list[0]]) * (count_num[num_list[0]] - 1) / 2 * (
                            count_num[target - num_list[0] - num_list[0]])

                        elif num_list[1] == num_list[0] or num_list[1] == num_list[2]:
                            result += (count_num[num_list[1]]) * (count_num[num_list[1]] - 1) / 2 * (
                            count_num[target - num_list[1] - num_list[1]])
                        else:
                            result += (count_num[num_list[2]]) * (count_num[num_list[2]] - 1) / 2 * (
                            count_num[target - num_list[2] - num_list[2]])
                    # print(result)

                    cal_list.append(num_list)

            if i == len(count_num.keys()) - 1:
                break

        return answer(int(result))


# Runtime: 929 ms, faster than 39.53% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.3 MB, less than 7.56% of Python3 online submissions for 3Sum With Multiplicity.
