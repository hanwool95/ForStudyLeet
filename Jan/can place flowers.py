class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        if n == 0:
            return True
        if len(flowerbed) <= 2:
            if 1 in flowerbed:
                return False
            else:
                return n < 2
        count = 0

        prev_zero = False
        for i, flower in enumerate(flowerbed):
            if flower == 0:
                if i == len(flowerbed)-1:
                    if prev_zero:
                        count += 1
                    break
                elif (i == 0) & (flowerbed[1] == 0):
                    count += 1
                    prev_zero = False
                elif prev_zero & (flowerbed[i+1] == 0):
                    count += 1
                    prev_zero = False
                else:
                    prev_zero = True
            else:
                prev_zero = False
        return n <= count
