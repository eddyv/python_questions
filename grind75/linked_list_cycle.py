# Definition for singly-linked list.
from typing import Optional, Set


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def helper(self, node: Optional[ListNode], visited: Set[ListNode]) -> bool:
        pass

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer != slow_pointer:
            if not fast_pointer or not fast_pointer.next:
                return False
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return True
