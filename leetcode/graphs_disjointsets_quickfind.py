# UnionFind class
class UnionFind:
    def __init__(self, size):
        # initialize the graph array to point to itself (each node is its own root)
        self.root = [i for i in range(size)]

    # O(1)
    def find(self, x):
        return self.root[x]

    # O(n)
    def union(self, x, y):
        """
        When connecting two vertices, store the root node for each vertex
        :param x: vertex
        :param y: vertex
        :return: None
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # we need to traverse through all the nodes to replace all roots with rootY to now point to rootX
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    # O(1) as find is quick af.
    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    # Test Case
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true