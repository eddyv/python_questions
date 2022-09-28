class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            pass
        if self.head.data == target_node_data:
            new_node.next = self.head.next
            self.head.next = new_node
        current_node = self.head
        while current_node.next:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            pass
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        current_node = self.head.next
        if current_node:
            while current_node.next:
                if current_node.data == target_node_data:
                    prev_node.next = new_node
                    new_node.next = current_node
                    return
                prev_node = current_node
                current_node = current_node.next

    def remove_node(self, target_node_data):
        if self.head is None:
            pass
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.data == target_node_data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    first_node = Node("a")
    llist.head = first_node
    print(llist)

    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    print(llist)

    llist = LinkedList(["a", "b", "c", "d", "e"])
    print(llist)
    for node in llist:
        print(node)
    llist.add_first(Node('x'))
    llist.add_last(Node('z'))
    print(llist)
