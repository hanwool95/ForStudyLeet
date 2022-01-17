class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        string_list = s.split(' ')
        result = True
        if len(string_list) != len(pattern):
            return False
        for pat in pattern:
            word = string_list.pop(0)
            if pat in pattern_dict.keys():
                if pattern_dict[pat] != word:
                    result = False
                    break
            else:
                if word in pattern_dict.values():
                    result = False
                    break
                pattern_dict[pat] = word

        return result