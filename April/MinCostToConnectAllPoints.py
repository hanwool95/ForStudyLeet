# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


#1 First Trial

import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_que = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cur_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(min_que, (cur_dist, i, j))

        result = 0
        connection_list = []

        def is_connection(x, y):
            for connection in connection_list:
                if x in connection and y in connection:
                    return True
            return False

        def write_connection(x, y):
            not_connect = True
            connection_target = None

            for connection in connection_list:
                if x in connection or y in connection:
                    if not_connect:
                        connection.append(x) if y in connection else connection.append(y)
                        not_connect = False
                        connection_target = connection
                    else:
                        for value in connection_target:
                            connection.append(value)
                        connection_list.remove(connection_target)
                        break

            if not_connect:
                connection_list.append([x, y])

        while min_que:
            cur_point = heapq.heappop(min_que)
            if not is_connection(cur_point[1], cur_point[2]):
                result += cur_point[0]
                write_connection(cur_point[1], cur_point[2])

        return result

# 모든 edge 집합 만드는 중 set을 활용하여 중복 찾는 작업이 O(n)을 잡아먹는 것을 확인 -> n+1 index부터 조회하는 방식으로 전환.
# heap Queue를 활용해서 우선순위가 낮은 노선을 뽑아내고 연결을 시키는 방법 사용.
# 정답을 도출하기는 하지만 긴 dot를 넣었을 때 Time limit 걸려서  Time Limit Exceeded 걸림.
# 연결 시키는지 여부를 파악할 때 시간 효율성이 O(n^2)이 걸리는 것이 문제라고 파악.




# 찾는 과정을 O(n)으로 만들기 위해서 연결 그룹을 1차원 평면화해야 함.

class Solution:
    connect_count = 0

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_que = []

        point_list = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cur_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(min_que, (cur_dist, i, j))
        result = 0
        connection_list = [x for x in range(len(points))]
        weight_list = [0 for x in range(len(points))]

        def is_connection(x, y):
            if connection_list[x] == connection_list[y]:
                return True
            write_connection(x, y)
            return False

        def find_group(group):
            return [i for i, value in enumerate(connection_list) if value == group]

        def write_connection(x, y):
            x = x if x == connection_list[x] else connection_list[x]
            y = y if y == connection_list[y] else connection_list[y]

            if weight_list[x] >= weight_list[y]:
                y_group = find_group(y)
                for index in y_group:
                    connection_list[index] = x
                if weight_list[x] == weight_list[y]:
                    weight_list[x] += 1
            else:
                x_group = find_group(x)
                for index in x_group:
                    connection_list[index] = y

            self.connect_count += 1

        while min_que:
            cur_point = heapq.heappop(min_que)
            if not is_connection(cur_point[1], cur_point[2]):
                result += cur_point[0]

            if self.connect_count == len(points) - 1:
                return result
        return result

# Runtime: 1736 ms, faster than 74.04% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 81.2 MB, less than 74.54% of Python3 online submissions for Min Cost to Connect All Points.