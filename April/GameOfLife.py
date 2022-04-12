# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        def count_live_neighbor(x, y, past_board):
            count = 0

            if x > 0:

                if past_board[y][x - 1] == 1:
                    count += 1

                if y > 0:
                    if past_board[y - 1][x - 1] == 1:
                        count += 1

                if y < len(past_board) - 1:
                    if past_board[y + 1][x - 1] == 1:
                        count += 1

            if x < len(past_board[0]) - 1:

                if past_board[y][x + 1] == 1:
                    count += 1

                if y > 0:
                    if past_board[y - 1][x + 1] == 1:
                        count += 1

                if y < len(past_board) - 1:
                    if past_board[y + 1][x + 1] == 1:
                        count += 1

            if y > 0:
                if past_board[y - 1][x] == 1:
                    count += 1

            if y < len(past_board) - 1:
                if past_board[y + 1][x] == 1:
                    count += 1

            return count

        past_board = copy.deepcopy(board)

        for i, x_list in enumerate(board):
            for j, cell in enumerate(x_list):
                count = count_live_neighbor(j, i, past_board)
                if cell == 1:
                    if count < 2 or count > 3:
                        # print("change 0")
                        board[i][j] = 0

                else:
                    if count == 3:
                        # print("change 1")
                        board[i][j] = 1


# Runtime: 48 ms, faster than 48.10% of Python3 online submissions for Game of Life.
# Memory Usage: 14 MB, less than 51.25% of Python3 online submissions for Game of Life.