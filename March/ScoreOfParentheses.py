# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following rule:
#
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def gain_score(string):
            if string == "()":
                return 1
            elif string == "":
                return 0
            elif string[0:2] == "()":
                return 1 + gain_score(string[2:])
            elif string[-2:] == "()":
                return gain_score(string[:-2]) + 1
            else:
                l_count = 0
                r_count = 0

                for word in string:
                    if word == "(":
                        l_count += 1
                    else:
                        r_count += 1
                    if l_count == r_count:
                        break

                return 2 * gain_score(string[1:l_count + r_count - 1]) + gain_score(string[l_count + r_count:])

        return gain_score(s)

# Runtime: 28 ms, faster than 94.45% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 13.9 MB, less than 30.17% of Python3 online submissions for Score of Parentheses.