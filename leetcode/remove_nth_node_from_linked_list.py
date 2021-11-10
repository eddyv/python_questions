# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_node = head
        nth_node = head
        curr_node = head
        distance_from_node = 0
        while curr_node:
            distance_from_node += 1
            curr_node = curr_node.next
            if distance_from_node > n:
                # the node to hook onto
                prev_node = nth_node
                # the node to remove
                nth_node = nth_node.next
                distance_from_node -= 1
        # if we need to remove the head, move the head pointer to the next node
        if nth_node == head:
            head = nth_node.next
        else:
            # otherwise we remove the nth element
            prev_node.next = nth_node.next
        return head
