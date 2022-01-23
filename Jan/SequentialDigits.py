class Solution:
    def make_seq(self, head, digit):
        current = head + digit
        if digit == 1:
            return current
        return int(current + self.make_seq(current / 10, digit / 10))

    def sequentialDigits(self, low: int, high: int) -> List[int]:

        low_digit = math.floor(math.log10(low))
        high_digit = math.floor(math.log10(high))

        remain_digit = high_digit - low_digit + 1

        result_lst = []
        cur_digit = low_digit
        for i in range(remain_digit):
            init_number = 10 ** cur_digit
            digit_10 = 10 ** cur_digit
            if i == 0:
                init_number = math.floor(low / init_number) * init_number
            cur_number = self.make_seq(init_number - digit_10, digit_10)
            while (cur_number < 10 ** (cur_digit + 1)) | \
                    cur_number < (10 ** (cur_digit + 1) - (cur_digit * 10 ** cur_digit)):
                if cur_number > high:
                    break
                if cur_number >= low:
                    result_lst.append(cur_number)
                init_number += digit_10
                cur_number = self.make_seq(init_number - digit_10, digit_10)
            cur_digit += 1

        return (result_lst)


