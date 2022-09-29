from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        mem = defaultdict(int)
        mem[1] = 1
        mem[2] = 2
        for i in range(3, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2]
        return mem[n]
