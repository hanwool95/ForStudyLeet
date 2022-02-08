class Solution:
    def addDigits(self, num: int) -> int:

        def add_two_digit(num):
            if num > 9:
                ten = num // 10
                one = num % 10
                return add_two_digit(ten + one)
            else:
                return num

        return add_two_digit(num)