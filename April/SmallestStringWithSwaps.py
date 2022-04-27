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





