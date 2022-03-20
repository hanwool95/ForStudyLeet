# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
#
# If it cannot be done, return -1.


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_count = Counter(tops)
        bot_count = Counter(bottoms)
        top_key = 0
        bot_key = 0

        for key in top_count.keys():
            top_key = key
            break
        for key in bot_count.keys():
            bot_key = key
            break

        i = 0

        print(top_key)
        print(bot_key)

        top_diff1 = 0
        top_diff2 = 0
        bot_diff1 = 0
        bot_diff2 = 0
        top_possible1 = True
        top_possible2 = True
        bot_possible1 = True
        bot_possible2 = True

        while i < len(tops):
            if top_possible1:
                if tops[i] != top_key:
                    if bottoms[i] == top_key:
                        top_diff1 += 1
                    else:
                        top_possible1 = False
            if top_possible2:
                if tops[i] != bot_key:
                    if bottoms[i] == bot_key:
                        top_diff2 += 1
                    else:
                        top_possible2 = False

            if bot_possible1:
                if bottoms[i] != bot_key:
                    if tops[i] == bot_key:
                        bot_diff1 += 1
                    else:
                        bot_possible1 = False
            if bot_possible2:
                if bottoms[i] != top_key:
                    if tops[i] == top_key:
                        bot_diff2 += 1
                    else:
                        bot_possible2 = False

            i += 1

        if not top_possible1 and not bot_possible1 and not top_possible2 and not bot_possible2:
            return -1
        else:
            possible_dict = {'0': top_possible1, '1': top_possible2, '2': bot_possible1, '3': bot_possible2}
            diff_list = [[top_diff1, '0'], [top_diff2, '1'], [bot_diff1, '2'], [bot_diff2, '3']]
            sort_list = diff_list.sort(key=lambda x: (x[0]))

            for number, key in diff_list:
                if possible_dict[key]:
                    return number
            return -1




# Runtime: 1569 ms, faster than 43.90% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.1 MB, less than 44.98% of Python3 online submissions for Minimum Domino Rotations For Equal Row.