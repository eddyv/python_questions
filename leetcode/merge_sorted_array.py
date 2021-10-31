class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_nums = list()

        nums1[m:m + n] = nums2[0:n]
        nums1.sort()