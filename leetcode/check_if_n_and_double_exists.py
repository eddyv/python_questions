class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        table = set(arr)
        for num in arr:
            # edge case
            if num == 0:
                if arr.count(num) > 1:
                    return True
            elif num * 2 in table:
                return True
        return False
