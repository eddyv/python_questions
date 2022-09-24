# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs:
                popped_char = stack.pop() if stack else None
                if pairs[char] != popped_char:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    sol = Solution()
    s = "()"
    answer = True
    assert (sol.isValid(s) == answer)
    s = "()[]{}"
    answer = True
    assert (sol.isValid(s) == answer)
    s = "(]"
    answer = False
    assert (sol.isValid(s) == answer)
    s = "}{"
    answer = False
    assert (sol.isValid(s) == answer)
    s = "()}{"
    answer = False
    assert (sol.isValid(s) == answer)
    s = "("
    answer = False
    assert (sol.isValid(s) == answer)
    s = ")"
    answer = False
    assert (sol.isValid(s) == answer)
