# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            # shift the current result one position to the left, add the next value using the 'or' operator
            head = head.next
            result = (result << 1) | head.val
        return result
