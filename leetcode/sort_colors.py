class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # assuming you cant use a library sort function
        # count the number of 0s(red), 1s(white), 2s(blue)

        # solution involves detecting the rightmost boundary of 0s, detecting the leftmost boundary of 2s and the current index
        leftmost_twos = len(nums) - 1
        current_index = 0
        rightmost_zeros = 0

        while current_index <= leftmost_twos:
            if nums[current_index] == 0:
                nums[current_index], nums[rightmost_zeros] = nums[rightmost_zeros], nums[current_index]
                rightmost_zeros += 1
                current_index += 1
            elif nums[current_index] == 2:
                nums[current_index], nums[leftmost_twos] = nums[leftmost_twos], nums[current_index]
                leftmost_twos -= 1
            elif nums[current_index] == 1:
                current_index += 1
