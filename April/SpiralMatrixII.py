# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result_list = []
        for i in range(n):
            x_row = []
            for j in range(n):
                x_row.append(0)
            result_list.append(x_row)

        State = "Right"

        count = 1

        right_max = n - 1
        down_max = n - 1
        left_min = 0
        up_min = 1

        cur_x = 0
        cur_y = 0

        for i in range(n * n):
            result_list[cur_y][cur_x] = count
            # print(cur_x, cur_y)
            if State == "Right":
                cur_x += 1
                if cur_x > right_max:
                    cur_x -= 1

                    State = "Down"
                    cur_y += 1

                    right_max -= 1

            elif State == "Down":
                cur_y += 1
                if cur_y > down_max:
                    cur_y -= 1
                    State = "Left"

                    cur_x -= 1

                    down_max -= 1

            elif State == "Left":
                cur_x -= 1
                if cur_x < left_min:
                    cur_x += 1
                    State = "Up"

                    cur_y -= 1

                    left_min += 1
            else:
                cur_y -= 1
                if cur_y < up_min:
                    cur_y += 1
                    State = "Right"

                    cur_x += 1

                    up_min += 1

            count += 1

        return result_list

# Runtime: 36 ms, faster than 81.42% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 13.9 MB, less than 41.06% of Python3 online submissions for Spiral Matrix II.



