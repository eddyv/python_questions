import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


# checks if a given binary search tree contains a given value.


def contains(root, value):
    if (root == None):
        return False
    if root.value == value:
        return True
    elif root.value > value:
        return contains(root.left, value)
    elif root.value < value:
        return contains(root.right, value)


#   Example case:
#   Correctness:
#   Performance test on a large tree:


# Binary search tree (BST) is a binary tree where the value of each node
# is larger or equal to the values in all the nodes in that node's left
# subtree and is smaller than the values in all the nodes in that node's right subtree.
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))
