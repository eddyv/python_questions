# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0 = head
        p1 = head

        while p0 and p0.next:
            p0 = p0.next.next
            p1 = p1.next

        return p1
