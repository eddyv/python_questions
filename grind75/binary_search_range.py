from typing import List


# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0


class Solution:
    def search(self, nums: List[int]) -> int:
        # pick middle
        low = 0
        high = len(nums) - 1
        middle = (high - low) // 2

        while low <= high:
            middle = low + ((high - low) // 2)
            if isCorrect(nums[middle]) == 0:
                return middle
            elif isCorrect(nums[middle]) < 0:
                # traverse the right side as the target is higher
                low = middle + 1
            else:
                high = middle - 1
        return -1