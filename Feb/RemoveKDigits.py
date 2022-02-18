class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count = k
        result = num[0]
        i = 1
        while count != 0 and i < len(num) - 1:
            if result[-1] > num[i + 1]:
                count -= 1
                while result[-1] > num[i + 1] and count != 0:
                    result = result[:-1]
                    count -= 1
            else:
                result += num[i]
            i += 1
        if result[-1] > num[i]:
            while result[-1] > num[i] and count != 0:
                result = result[:-1]
                count -= 1
            result += num[i]

        if i < len(num) - 1:
            result += num[i:]
        if count > 0:
            result = result[:-count]
        result = result.lstrip("0")
        if result == "":
            return "0"
        else:
            return result