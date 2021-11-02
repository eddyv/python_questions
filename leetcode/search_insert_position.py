from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        elif nums[right] < target:
            return right + 1
        elif nums[left] < target:
            return right


if __name__ == '__main__':
    sol = Solution()
    ex1 = [1, 3, 5, 6]
    assert (sol.searchInsert(nums=ex1, target=7) == 4)
