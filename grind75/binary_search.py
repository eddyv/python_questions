class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pick middle
        low = 0
        high = len(nums) - 1
        middle = (high - low) // 2

        while low <= high:
            middle = low + ((high - low) // 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                # traverse the right side as the target is higher
                low = middle + 1
            else:
                high = middle - 1
        return -1
