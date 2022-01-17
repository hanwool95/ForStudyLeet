class Solution(object):
    def findJudge(self, n, trust):
        count_lst = [0 for i in range(n)]
        judge_lst = [0 for i in range(n)]

        for judge, trusted in trust:
            count_lst[trusted - 1] += 1
            judge_lst[judge - 1] += 1
        max_int = max(count_lst)
        if max_int == n-1:
            result = count_lst.index(max_int) + 1
        else:
            result = -1

        if min(judge_lst) >= 1:
            result = -1

        count = 0
        for num in count_lst:
            if num == max_int:
                count += 1

        if count >= 2:
            result = -1


        return result

n = 2
trust = [[1,2]]


s = Solution()

print(s.findJudge(n, trust))