class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        current_list = []
        for word in s:
            if word in current_list:
                if len(current_list) > max_num:
                    max_num = len(current_list)
                inx = current_list.index(word)
                current_list = current_list[inx + 1:]
                current_list.append(word)
            else:
                current_list.append(word)
        if len(current_list) > max_num:
            max_num = len(current_list)

        return max_num

