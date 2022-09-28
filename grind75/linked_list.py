class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        # dummy node which makes removing a node from the start easier
        self.head = self.tail = Node(-1)

    def insertEnd(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def insertStart(self, val):
        old_head = self.head.next
        new_head = Node(val)
        self.head.next = new_head
        if old_head:
            new_head.next = old_head

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        # remove the node ahead of curr
        if curr:
            if curr.next:
                curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(f'{curr.val}->', end='')
            curr = curr.next
        print()


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertEnd(3)
    ll.print()
    ll.insertStart(2)
    ll.print()
    ll.insertStart(1)
    ll.print()
    ll.insertEnd(4)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.remove(0)
    ll.print()
    ll.insertEnd(1)
    ll.print()