class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, compute and return the square root of x.
        Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result
        is returned.
        Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
        Example 1:
            Input: x = 4
            Output: 2
        Example 2:
            Input: x = 8
            Output: 2
            Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
        Constraints:
            0 <= x <= 2^31 - 1
        """
        # base case
        if x < 2:
            return x

        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2  # a + (b - a) / 2. A precaution to avoid overflow
            num_squared = mid * mid
            if num_squared == x:
                return mid
            elif num_squared < x:
                left = mid + 1
            elif num_squared > x:
                right = mid - 1

        # in some cases, the sqrt(x) is not a whole number,
        # so once left <= right we want to return the right pointer as it's the "smallest" between left and right
        return right


if __name__ == '__main__':
    sol = Solution()
    assert (sol.mySqrt(4) == 2)
    assert (sol.mySqrt(8) == 2)
    assert (sol.mySqrt(9) == 3)
