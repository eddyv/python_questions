from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        """
        Constraints:
            - 1 <= nums.length <= 105
            - nums[i] is either 0 or 1.

        example:
        Input: nums = [1,0,1,1,0]
        Output: 4
        Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
        Input: nums = [1,0,1,1,0,1]
        Output: 4
        """
        # To complete this problem we will use a sliding window.

        start_pos = 0
        end_pos = 0
        max_consecutive_ones = 0
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
                # its time to shrink our sliding window
                while zero_counter > 1:
                    if nums[start_pos] == 0:
                        zero_counter -= 1
                    start_pos += 1
            end_pos += 1
            max_consecutive_ones = max(max_consecutive_ones, end_pos - start_pos)
        return max_consecutive_ones


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    assert (Solution.findMaxConsecutiveOnes(nums) == 4)
    nums = [1, 0, 1, 1, 0, 1]
    assert (Solution.findMaxConsecutiveOnes(nums) == 4)
    nums = [0, 0, 1, 1, 1, 1]
    assert (Solution.findMaxConsecutiveOnes(nums) == 5)
