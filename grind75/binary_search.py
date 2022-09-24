class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums is sorted
        # pick middle

        middle_index = (len(nums) - 1) // 2
        middle = nums[middle_index]
        if middle == target:
            return middle_index
        elif len(nums) == 1:
            return -1
        else:
            return self.search()

