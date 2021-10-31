class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        num_not_ordered = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                num_not_ordered +=1
        return num_not_ordered