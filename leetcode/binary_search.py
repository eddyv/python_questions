from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
        search target in nums. If target exists, then return its index. Otherwise, return -1.

        Example 1:
            Input: nums = [-1,0,3,5,9,12], target = 9
            Output: 4
            Explanation: 9 exists in nums and its index is 4

        Example 2:
            Input: nums = [-1,0,3,5,9,12], target = 2
            Output: -1
            Explanation: 2 does not exist in nums so return -1

        Constraints:
            1 <= nums.length <= 104
            -104 < nums[i], target < 104
            All the integers in nums are unique.
            nums is sorted in ascending order.
        """
        start_index = 0
        # start_index + (end_index - start_index)/ 2
        end_index = len(nums) - 1

        # terminate when start > end a.k.a we cant find the target
        while start_index <= end_index:
            # avoid overflow by using a + (b-a) / 2
            mid_index = start_index + (end_index - start_index) // 2
            if nums[mid_index] == target:
                return mid_index
            # search right side
            elif nums[mid_index] > target:
                end_index = mid_index - 1
            # search left side
            elif nums[mid_index] < target:
                start_index = mid_index + 1
        # not found
        return -1


if __name__ == '__main__':
    sol = Solution()
    ex1 = [-1, 0, 3, 5, 9, 12]
    assert (sol.search(nums=ex1, target=9) == 4)
    assert (sol.search(nums=ex1, target=2) == -1)
    ex2 = [-1, 0]
    assert (sol.search(nums=ex2, target=1) == -1)
    assert (sol.search(nums=ex2, target=-1) == 0)
    assert (sol.search(nums=ex2, target=0) == 1)
    ex3 = [-1, 0, 1]
    assert (sol.search(nums=ex3, target=1) == 2)
    assert (sol.search(nums=ex3, target=0) == 1)
    assert (sol.search(nums=ex3, target=-1) == 0)
