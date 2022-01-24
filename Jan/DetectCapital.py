class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result = False
        is_all_C = True
        is_all_S = True
        for i, s in enumerate(word):
            if i == 0:
                if s.isupper():
                    result = True
                    is_all_S = False
                else:
                    is_all_C = False
            else:
                if s.isupper():
                    result = False
                    is_all_S = False
                else:
                    is_all_C = False

        if is_all_C or is_all_S:
            return True
        else:
            return result



