# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
# In one shift operation:
#
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        result_list = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            new_row = []
            for j in range(n):
                new_row.append(None)
            result_list.append(new_row)

        for i, x_list in enumerate(grid):
            for j, value in enumerate(x_list):
                cur_one_D = (i * n + j + k) % (m * n)
                new_x = cur_one_D // n
                new_y = cur_one_D % n

                result_list[new_x][new_y] = value

        return result_list


# Runtime: 216 ms, faster than 61.28% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 14.4 MB, less than 13.09% of Python3 online submissions for Shift 2D Grid.