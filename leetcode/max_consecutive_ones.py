from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currCount = 0
        for num in nums:
            if num == 1:
                currCount += 1
            else:
                maxOnes = max(maxOnes, currCount)
                currCount = 0

        return max(maxOnes, currCount)