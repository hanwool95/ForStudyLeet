class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        len_1 = len(nums1)
        len_2 = len(nums2)
        len_merged = len(merged_list)
        median = 0
        if len_merged % 2 == 0:
            median = (merged_list[int(len_merged / 2) - 1] + merged_list[int(len_merged / 2)]) / 2
        else:
            median = merged_list[int(len_merged / 2)]
        return median
