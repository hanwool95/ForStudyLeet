# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.


# First Trial

class Solution:

    def execute_route(self, routes, s):
        for route in routes:
            s = self.switching_route(route[0], route[1], s)
        return s

    def switching_route(self, p1, p2, s):
        o1 = s[p1]
        o2 = s[p2]
        s = "".join((s[:p1], o2, s[p1 + 1:]))
        s = "".join((s[:p2], o1, s[p2 + 1:]))
        return s

    def finding_route(self, index, routes, string):
        start = index
        min_route = []
        min_word = string[index]
        cur_route = []
        min_route = self.recursive_route(cur_route, routes, string, start, min_word, min_route)
        return min_route if min_route else []

    def recursive_route(self, cur_route, routes, string, start, min_word, min_route):
        recur_route = cur_route
        for route in routes:
            if route[0] == start and string[route[1]] < min_word:
                # print(route)
                recur_route.insert(0, route)
                min_route = recur_route
                min_word = string[route[1]]
                self.recursive_route(recur_route, routes, string, route[1], min_word, min_route)
        return min_route

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        index = 0
        while index < len(s) / 2:
            route = self.finding_route(index, pairs, s)
            print(route)

            s = self.execute_route(route, s)
            print(s)
            index += 1

        return s


# 첫 단어부터 한 글자씩 최소 단어로 바꾸는 방법을 사용.
# 경로 찾는 함수, 경로 바탕으로 글자 바꾸는 함수 구현 완료
# 함수 자체에는 문제가 없지만, 풀이 접근 방식에 오류가 있었음. 앞 단어를 건드려야 나머지가 최소 값이 되는 경우에 오답을 제출.




# Second Trial
# 연결된 점들은 서로 바꿀 수 있음. 따라서 grouping 방식으로 문제 해결 가능.
# 어제 문제(MinCostToConnectAllPoints) 적용한 1차원 group을 사용.

class Solution:
    def findGroup(self, pairs, group, weight):

        for p1, p2 in pairs:
            p1G = self.discover(p1, group)
            p2G = self.discover(p2, group)
            if p1G != p2G:

                if weight[p1G] >= weight[p2G]:

                    for i, index in enumerate(group):
                        if index == p2G:
                            group[i] = p1G

                    group[p2G] = p1G
                    if weight[p1G] == weight[p2G]:
                        weight[p1G] += 1
                else:
                    for i, index in enumerate(group):
                        if index == p1G:
                            group[i] = p2G

    def discover(self, p, group):
        if p != group[p]:
            return self.discover(group[p], group)
        return p

    def executeSet(self, group, s):
        group_list = set(group)
        group_dict = {}

        for cur_group in group_list:
            group_dict[cur_group] = []

        for i, index in enumerate(group):
            group_dict[index].append(i)

        for group_index, value_list in group_dict.items():
            cur_str = ""
            for value in value_list:
                cur_str += s[value]
            sorted(cur_str)
            cur_str = ''.join(sorted(cur_str))

            for i in range(len(cur_str)):
                s = ''.join((s[:value_list[i]], cur_str[i], s[value_list[i] + 1:]))
        return s

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        group = [x for x in range(len(s))]
        weight = [0 for i in range(len(s))]

        self.findGroup(pairs, group, weight)
        s = self.executeSet(group, s)

        return s


# 정답은 찾아 나감.
# 하지만 time limit. 단순히 O(n^2)로는 통과가 안되는 것으로 보임.




# Third Trial
# Grouping 에서 Dictionary를 활용. 최대한 runtime 줄이는 방향

class Groups:

    def __init__(self, s):
        self.group = [x for x in range(len(s))]
        self.weight = [0 for i in range(len(s))]
        self.Gdict = {}

    def discover(self, p):
        if p != self.group[p]:
            return self.discover(self.group[p])
        return self.group[p]

    def grouping(self, parent, target):
        self.group[target] = parent
        if self.weight[parent] == 0:
            self.Gdict[parent] = []

        if self.weight[target] > 0:
            for x in self.Gdict[target]:
                self.Gdict[parent].append(x)
            self.Gdict[parent].append(target)
            del self.Gdict[target]
        else:
            self.Gdict[parent].append(target)

    def findGroup(self, pairs):
        for p1, p2 in pairs:
            p1G = self.discover(p1)
            p2G = self.discover(p2)
            if p1G != p2G:

                if self.weight[p1G] >= self.weight[p2G]:

                    self.grouping(p1G, p2G)

                    if self.weight[p1G] == self.weight[p2G]:
                        self.weight[p1G] += 1


                else:
                    self.grouping(p2G, p1G)


class Solution:
    def executeSet(self, group_dict, s):

        for group_index, value_list in group_dict.items():
            cur_str = ""
            value_list.append(group_index)
            value_list.sort()
            for value in value_list:
                cur_str += s[value]
            sorted(cur_str)
            cur_str = ''.join(sorted(cur_str))

            for i in range(len(cur_str)):
                s = ''.join((s[:value_list[i]], cur_str[i], s[value_list[i] + 1:]))
        return s

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        Group = Groups(s)

        Group.findGroup(pairs)
        s = self.executeSet(Group.Gdict, s)

        return s

Runtime: 3292 ms, faster than 5.06% of Python3 online submissions for Smallest String With Swaps.
Memory Usage: 50.5 MB, less than 43.32% of Python3 online submissions for Smallest String With Swaps.