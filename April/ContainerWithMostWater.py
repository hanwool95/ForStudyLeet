# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


class Solution:
    maxNum = 0

    def maxArea(self, height: List[int]) -> int:

        def contain_water(left, right, length):

            height = min(left, right)
            width = length - 1

            return height * width

        def compare_max(value):
            if value > self.maxNum:
                self.maxNum = value

#         def find_max(height_list):
#             if len(height_list) == 2:
#                 return compare_max(min(height_list[0], height_list[1]))

#             compare_max(contain_water(height_list))

#             if height_list[0] > height_list[-1]:
#                 find_max(height_list[:-1])
#             else:
#                 find_max(height_list[1:])

        cur_left = 0
        cur_right = len(height) - 1
        length = len(height)

        while cur_left != cur_right:
            compare_max(contain_water(height[cur_left], height[cur_right], length))

            if height[cur_left] > height[cur_right]:
                cur_right -= 1
            else:
                cur_left += 1

            length -= 1

        return self.maxNum

# Runtime: 959 ms, faster than 50.65% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.9 MB, less than 17.98% of Python3 online submissions for Container With Most Water.
