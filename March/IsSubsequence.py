class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        cur_index = 0
        remain = len(s)
        for word in t:
            if word == s[cur_index]:
                cur_index += 1
                remain -= 1
                if remain == 0:
                    return True
        return False