# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def helper(self, node: Optional[TreeNode]) -> (int, bool):
        if not node:
            return -1, True

        left_h, left_is_balanced = self.helper(node.left)
        right_h, right_is_balanced = self.helper(node.right)
        if not left_is_balanced or not right_is_balanced:
            return 0, False

        return 1 + max(left_h, right_h), (abs(left_h - right_h) < 2)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]
