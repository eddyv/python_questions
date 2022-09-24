from typing import List


# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_seen = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in num_seen:
                return [num_seen[difference], index]
            else:
                num_seen[value] = index


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    answer = [0, 1]
    assert (sol.twoSum(nums, target) == answer)
    nums = [3, 2, 4]
    target = 6
    answer = [1, 2]
    assert (sol.twoSum(nums, target) == answer)
    nums = [3, 3]
    target = 6
    answer = [0, 1]
    assert (sol.twoSum(nums, target) == answer)
