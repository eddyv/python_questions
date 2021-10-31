class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_occurences = nums.count(val)
        num_elements = len(nums) - num_occurences
        i = 0
        while i < num_occurences:
            nums.remove(val)
            i += 1
        return num_elements
