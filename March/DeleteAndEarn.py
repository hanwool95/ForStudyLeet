class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_num = Counter(nums)

        max_num = max(count_num.keys())

        @cache
        def max_result(number):
            if number == 1:
                if 1 in count_num.keys():
                    return count_num[1]
                else:
                    return 0
            elif number == 0:
                return 0
            current = 0
            if number in count_num.keys():
                current = number * count_num[number]
            return max(max_result(number - 1), max_result(number - 2) + current)

        return max_result(max_num)

        # for number, count in sort_num:
        #     if prev_num + 1 == number:
        #         if odd:
        #             odd_sum += number * count
        #             odd = False
        #         else:
        #             even_sum += number * count
        #             odd = True
        #     else:
        #         result += odd_sum if odd_sum > even_sum else even_sum
        #         odd_sum = number * count
        #         even_sum = 0
        #         odd = False
        #     #print(result)
        #     prev_num = number
        # print(odd_sum)
        # print(even_sum)
        # result += odd_sum if odd_sum > even_sum else even_sum

#         return result