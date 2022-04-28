# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


# First Trial
# 모든 경우의 수를 recursive하게 둘러 본 뒤, 그 경로로 갔을 때 나올 수 있는 가장 작은 heights를 받은 뒤 그 중 최소 값을 return 하는 방식으로 작성해봄.

class checking_bot:
    def __init__(self, heights):
        self.heights = heights
        self.max_x = len(self.heights[0]) - 1
        self.max_y = len(self.heights) - 1
        self.global_min = 101

    def is_valid(self, direction, x, y, path):
        if direction == "left":
            return True if x > 0 and [x - 1, y] not in path else False
        elif direction == "right":
            return True if x < self.max_x and [x + 1, y] not in path else False
        elif direction == "down":
            return True if y < self.max_y and [x, y + 1] not in path else False
        elif direction == "up":
            return True if y > 0 and [x, y - 1] not in path else False
        else:
            print("wrong direction error")

    def finding_route(self, x, y, cur_min, path):
        if x == self.max_x and y == self.max_y:
            if cur_min < self.global_min:
                self.global_min = cur_min
            return cur_min

        if cur_min > self.global_min:
            return cur_min

        min_list = []

        if self.is_valid("left", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y][x - 1])
            new_path = path + [[x - 1, y]]
            min_list.append(self.finding_route(x - 1, y, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("right", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y][x + 1])
            new_path = path + [[x + 1, y]]
            min_list.append(self.finding_route(x + 1, y, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("down", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y + 1][x])
            new_path = path + [[x, y + 1]]
            min_list.append(self.finding_route(x, y + 1, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("up", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y - 1][x])
            new_path = path + [[x, y - 1]]
            min_list.append(self.finding_route(x, y - 1, cur_min if cur_min > diff else diff, new_path))

        return min(min_list) if len(min_list) > 0 else 101


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == 1 and len(heights[0]) == 1:
            return 0

        bot = checking_bot(heights)

        return bot.finding_route(0, 0, -1, [[0, 0]])

# 모든 경로를 찾는 방법이기에 속도 효율이 좋지 않음.
# 정답은 잘 도출하지만 Time limit 제한에 걸림.





# Second Trial
# 첫 번째 시도에서 사용한 코드에서 최적화 시도.
# 글로벌 최소 값을 정해서 만약 경로 중에 글로벌 최소값을 넘기면 중단되는 코드 추가
# 해당 경로의 가능한 최소값을 저장하는 logic 추가.

class checking_bot:
    def __init__(self, heights):
        self.heights = heights
        self.max_x = len(self.heights[0]) - 1
        self.max_y = len(self.heights) - 1
        self.global_min = 101
        self.min_dict = {}

    def is_valid(self, direction, x, y, path):
        if direction == "left":
            return True if x > 0 and [x - 1, y] not in path else False
        elif direction == "right":
            return True if x < self.max_x and [x + 1, y] not in path else False
        elif direction == "down":
            return True if y < self.max_y and [x, y + 1] not in path else False
        elif direction == "up":
            return True if y > 0 and [x, y - 1] not in path else False
        else:
            print("wrong direction error")

    def finding_route(self, x, y, cur_min, path):
        if x == self.max_x and y == self.max_y:
            if cur_min < self.global_min:
                self.global_min = cur_min
            return cur_min

        route_string = str(x) + str(y)

        if route_string in self.min_dict.keys():
            if self.min_dict[route_string] < cur_min:
                return self.min_dict[route_string]

        if cur_min > self.global_min:
            return cur_min

        min_list = []

        if self.is_valid("left", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y][x - 1])
            new_path = path + [[x - 1, y]]
            min_list.append(self.finding_route(x - 1, y, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("right", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y][x + 1])
            new_path = path + [[x + 1, y]]
            min_list.append(self.finding_route(x + 1, y, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("down", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y + 1][x])
            new_path = path + [[x, y + 1]]
            min_list.append(self.finding_route(x, y + 1, cur_min if cur_min > diff else diff, new_path))

        if self.is_valid("up", x, y, path):
            diff = abs(self.heights[y][x] - self.heights[y - 1][x])
            new_path = path + [[x, y - 1]]
            min_list.append(self.finding_route(x, y - 1, cur_min if cur_min > diff else diff, new_path))

        minimum = min(min_list) if len(min_list) > 0 else 101

        self.min_dict[route_string] = minimum

        return minimum


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == 1 and len(heights[0]) == 1:
            return 0

        bot = checking_bot(heights)

        return bot.finding_route(0, 0, -1, [[0, 0]])

# 그래도 time limit에 걸리는 방법


# Third Trial
# 다익스트라 알고리즘 활용하여 프로그램 변형.
# 방문한 지점의 방문 여부 저장, 방문 지점 주변의 최단거리 저장.
# 방문 지점 주변 중에서 방문하지 않는 곳은 pq에 저장.
# pq 순서에 따라서 방
# 목표 지점 도달했을 때 목표 지점의 최단 거리 return.


from queue import PriorityQueue


class Checking_bot:
    def __init__(self, heights, que):
        self.heights = heights
        self.max_x = len(self.heights[0]) - 1
        self.max_y = len(self.heights) - 1

        self.visited = [[False] * (self.max_x + 1) for i in range(self.max_y + 1)]
        self.min_dist = [[float("inf")] * (self.max_x + 1) for i in range(self.max_y + 1)]
        self.min_dist[0][0] = 0

        self.priorq = que
        self.priorq.put((0, (0, 0)))

    def is_valid(self, direction, x, y):
        if direction == "left":
            return True if x > 0 and not self.visited[y][x - 1] else False
        elif direction == "right":
            return True if x < self.max_x and not self.visited[y][x + 1] else False
        elif direction == "down":
            return True if y < self.max_y and not self.visited[y + 1][x] else False
        else:
            return True if y > 0 and not self.visited[y - 1][x] else False

    def finding_route(self):

        while not self.visited[self.max_y][self.max_x]:
            cur_point = self.priorq.get()
            x = cur_point[1][0]
            y = cur_point[1][1]
            h = self.min_dist[y][x]

            self.visited[y][x] = True

            if self.is_valid("left", x, y):
                dist = abs(self.heights[y][x] - self.heights[y][x - 1])
                self.priorq.put((dist, (x - 1, y)))

                if self.min_dist[y][x - 1] > dist:
                    self.min_dist[y][x - 1] = dist if dist > h else h

            if self.is_valid("right", x, y):
                dist = abs(self.heights[y][x] - self.heights[y][x + 1])
                self.priorq.put((dist, (x + 1, y)))

                if self.min_dist[y][x + 1] > dist:
                    self.min_dist[y][x + 1] = dist if dist > h else h

            if self.is_valid("down", x, y):
                dist = abs(self.heights[y][x] - self.heights[y + 1][x])
                self.priorq.put((dist, (x, y + 1)))

                if self.min_dist[y + 1][x] > dist:
                    self.min_dist[y + 1][x] = dist if dist > h else h

            if self.is_valid("up", x, y):
                dist = abs(self.heights[y][x] - self.heights[y - 1][x])
                self.priorq.put((dist, (x, y - 1)))

                if self.min_dist[y - 1][x] > dist:
                    self.min_dist[y - 1][x] = dist if dist > h else h

        return self.min_dist[self.max_y][self.max_x]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == 1 and len(heights[0]) == 1:
            return 0

        que = PriorityQueue()

        bot = Checking_bot(heights, que)

        return bot.finding_route()

# Runtime: 1558 ms, faster than 35.17% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 16.3 MB, less than 44.28% of Python3 online submissions for Path With Minimum Effort.