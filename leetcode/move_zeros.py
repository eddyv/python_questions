class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_occurences = nums.count(0)
        i=0
        while i < num_occurences:
            nums.remove(0)
            nums.append(0)
            i+=1
        return nums