from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        # number of "clustered provinces"
        self.count = size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # the height of the x tree is higher than y, append y to x
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            # height of the y tree is higher than x, append x to y
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            # heights are the same, increase the rank of whoever we choose as the root as the height will then change
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            # this node is apart of a larger province, decrease count
            self.count -= 1

    def getCount(self):
        return self.count

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    """
    There are n cities. Some of them are connected, while some are not.
    If city a is connected directly with city b, and city b is connected directly with city c, then city a is
    connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    You are given an n x n matrix isConnected where isConnected[i][j] = 1
    if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
    Return the total number of provinces.
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.getCount()
