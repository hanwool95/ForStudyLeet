class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        is_increase = True
        if len(arr) == 1:
            return False
        for i, word in enumerate(arr):
            if i != 0:
                if i == 1:
                    if word < arr[i-1]:
                        return False
                if word == arr[i-1]:
                    return False
                if is_increase:
                    if word < arr[i-1]:
                        is_increase = False
                else:
                    if word > arr[i-1]:
                        return False
        if is_increase:
            return False
        else:
            return True