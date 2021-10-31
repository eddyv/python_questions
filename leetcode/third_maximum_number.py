from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

        Example 1:
            Input: nums = [3,2,1]
            Output: 1
            Explanation:
            The first distinct maximum is 3.
            The second distinct maximum is 2.
            The third distinct maximum is 1.

        Example 2:
            Input: nums = [1,2]
            Output: 2
            Explanation:
            The first distinct maximum is 2.
            The second distinct maximum is 1.
            The third distinct maximum does not exist, so the maximum (2) is returned instead.

        Example 3:
            Input: nums = [2,2,3,1]
            Output: 1
            Explanation:
            The first distinct maximum is 3.
            The second distinct maximum is 2 (both 2's are counted together since they have the same value).
            The third distinct maximum is 1.

        Constraints:
            - 1 <= nums.length <= 104
            - -231 <= nums[i] <= 231 - 1
        """
        maximum_nums = []  # keep track of the top 3 results... Keep them sorted!

        for num in nums:
            if maximum_nums.count(num) == 0:
                # fill in the number count
                if len(maximum_nums) < 3:
                    maximum_nums.append(num)
                else:
                    # only perform this check if the number is not present in the list
                    if num > maximum_nums[0]:
                        # no need to shift any numbers as they are already in the right spot
                        maximum_nums[0] = num
                    elif num > maximum_nums[1]:
                        # shift elements , set the new number in proper position
                        maximum_nums[1], maximum_nums[0] = num, maximum_nums[1]
                    elif num > maximum_nums[2]:
                        # shift elements, set the new number in proper position
                        maximum_nums[2], maximum_nums[1], maximum_nums[0] = num, maximum_nums[2], maximum_nums[1]
                # keep the list sorted
                maximum_nums.sort()

        if len(maximum_nums) < 3:
            return maximum_nums[-1]

        return maximum_nums[0]


if __name__ == '__main__':
    sol = Solution()
    ex1 = [3, 2, 1]
    assert (sol.thirdMax(nums=ex1) == 1)
    ex2 = [1, 2]
    assert (sol.thirdMax(nums=ex2) == 2)
    ex3 = [2, 2, 3, 1]
    assert (sol.thirdMax(nums=ex3) == 1)
