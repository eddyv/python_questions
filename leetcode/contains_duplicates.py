from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        if len(set_nums) < len(nums):
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    assert (sol.containsDuplicate(nums) is True)
    nums = [1, 2, 3, 4]
    assert (sol.containsDuplicate(nums) is False)
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert (sol.containsDuplicate(nums) is True)
