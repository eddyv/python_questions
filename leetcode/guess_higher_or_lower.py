# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = (2 ** 31 - 1)  # 2^31 -1
        num = n

        while left <= right:
            if guess(num) == 0:
                return num
            elif guess(num) > 0:
                left = num + 1
            elif guess(num) < 0:
                right = num - 1
            num = left + (right - left) // 2
