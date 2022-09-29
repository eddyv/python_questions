# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            middle = low + ((high - low) // 2)
            if isBadVersion(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low
