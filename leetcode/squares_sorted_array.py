class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda num: num * num, nums))
        nums.sort()
        return nums

