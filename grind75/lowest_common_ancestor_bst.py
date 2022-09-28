# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # start at root, check if the value of p and q. This will determine which side of the tree you are traversing
        # through. If they are both different, then you are the LCA. by virtue of a binary search tree property.

        # base case root=p or root=q or p>root>q or p<root<q
        print(f'root: {root.val}, p: {p.val}, q: {q.val}')
        if (root.val == p.val or
                root.val == q.val or
                p.val > root.val > q.val or
                p.val < root.val < q.val):
            return root
        else:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestorIter(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            print(f'root: {curr.val}, p: {p.val}, q: {q.val}')
            if (curr.val == p.val or
                    curr.val == q.val or
                    p.val > curr.val > q.val or
                    p.val < curr.val < q.val):
                return curr
            else:
                if p.val < curr.val and q.val < curr.val:
                    curr = curr.left
                if p.val > curr.val and q.val > curr.val:
                    curr = curr.right
