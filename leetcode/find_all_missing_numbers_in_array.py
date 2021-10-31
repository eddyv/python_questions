from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
        Constraints:
            n == nums.length
            1 <= n <= 105
            1 <= nums[i] <= n
        """
        missing_nums = set(range(1, len(nums)+1))
        num_set = set(nums)
        return list(missing_nums - num_set)


if __name__ == '__main__':
    sol = Solution()
    ex1 = [4, 3, 2, 7, 8, 2, 3, 1]
    assert (sol.findDisappearedNumbers(nums=ex1) == [5, 6])
    ex2 = [1, 1]
    assert (sol.findDisappearedNumbers(nums=ex2) == [2])
