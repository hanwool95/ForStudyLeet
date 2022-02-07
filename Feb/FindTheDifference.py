class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for word in t:
            if word not in s:
                return word
            else:
                s = s.replace(word,"", 1)