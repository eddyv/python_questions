from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        table = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in table:
                result.append(table[compliment])
                result.append(i)
            table[num] = i
        return result
