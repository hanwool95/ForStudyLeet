class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        natural = poured

        for i in range(query_row):
            natural -= 2 ** (i)

        if query_glass <= round((query_row - 1) / 2):
            floor = 2 ** (query_row - query_glass)
            if query_row > 3:
                if query_glass == round((query_row - 1) / 2):
                    for i in range(query_row - 2):
                        natural += 2 ** (i + 1)
                elif query_glass > 0:
                    for i in range(query_row - 1 + query_glass):
                        natural += 2 ** (i + 1)

        else:
            floor = 2 ** (query_glass)
            if query_row > 3 and query_glass < query_row:
                for i in range(query_row + 2 - query_glass):
                    natural += 2 ** (i + 1)

        if natural < 0:
            return 0

        return natural / floor if (natural / floor) < 1 else 1

# not resolved

# (N-0)*1/2^0
#
# (N-1)*1/2^1 (n-1)*1/2^1
#
# (N-1-2)*1/2^2 (n-1-2)*1/2^(2-1) (n-1-2)*1/4^2
#
# (N-1-2-4)*1/2^3 (n-1-2-4+2)*1/2^(3-1) (n-1-2-4+2)*1/2^(3-1) (n-1-2-4)*1/2^3
#
# (N-1-2-4-8)*1/2^4 (n-1-2-4-8+2+4)*1/2^(4-1) (n-1-2-4-8+2+4)*1/2^(4-2) (n-1-2-4-8+2+4)*1/2^(4-1) (N-1-2-4-8)*1/2^4
#
# (N-1-2-4-8-16)*1/2^5 (n-1-2-4-8-16+8)*1/2^(5-1) (n-1-2-4-8-16+2+4+8)*1/2^(5-2) (n-1-2-4-8+2+4)*1/2^(4-1) (N-1-2-4-8)*1/2^4
#
# 0 0
# 0 0 0
# 0 a a 0 1
# 0 a a a 0 2
# 0 a b b a 0 3, 4
# 0 a b b b a 0 4, 5
# 0 a b c c b a 0 5 6 7
# 0 a b c c c b a 0
#
# 0 1 1 0
# 0 2 2 2 0
#
# 0 3 4 4 3 0
# 0 1 2 3 4 5
#
# 0 4 5 6 5 4 0
# 0 5 6 7 7 6 5 0
#
# 0
#
#
#
# 층 기본 필요: N - ( 2^0 + 2^1 + … + 2^(row-1))
# 층 필요 보정:
# If (row-1)/2.round < 0:
# - glass
# Else:
# -(row-glass)
#
#
#
#
#
#
# 층 기본 pour: 2^row
# 층 pour 보정:
# If (row-1)/2.round < 0:
# - glass
# Else:
# -(row-glass)
#
# 0 1 0
# 0 1 2
# 2부터 2-
#
# 0 1 1 0
# 0 1 2 3
# 2부터 3-
#
# 0 1 2 1 0
# 0 1 2 3 4
# 3부터 4-
#
# 0 1 2 2 1 0
# 0 1 2 3 4 5
# 3부터 5-
#
#
#
# 0 1 2 1 0
# 0 1 2 3 4
#
# 0 1 2 3 2 1 0
