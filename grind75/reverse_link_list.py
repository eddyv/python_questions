# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseListIter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_node = None
        curr_node = head
        while curr_node:
            # save the next item in the list cause we are about to overwrite it
            next_node = curr_node.next
            # overwrite with the previous node
            curr_node.next = prev_node
            # our previous node now becomes our current node (otherwise we lose this pointer)
            prev_node = curr_node
            # move to our next node
            curr_node = next_node
        # return the last item in the list
        return prev_node
