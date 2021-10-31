class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # base case
        if len(arr) < 3:
            return False

        i = 1
        while i < len(arr) and arr[i - 1] < arr[i]:
            i += 1
        # no downhill detected or uphill detected
        if i == len(arr) or i == 1:
            return False
        while i < len(arr) and arr[i - 1] > arr[i]:
            i += 1
        # valid uphill and downhill
        if i == len(arr):
            return True
        return False