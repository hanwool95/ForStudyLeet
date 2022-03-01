class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]

        if n == 0:
            return result

        store = [1]
        result = result + store
        if n == 1:
            return result

        log2 = int(math.log(n, 2))
        remain = n - (2 ** log2)

        for i in range(log2 - 1):
            current = []
            for number in store:
                current.append(number + 1)
            store += current
            result += store

        for i in range(remain + 1):
            result.append(result[i] + 1)

        return result

