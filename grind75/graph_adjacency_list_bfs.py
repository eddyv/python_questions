from collections import deque
from typing import List, Dict


# shortest path from node to target
def bfs(node: str, target: str, adjList: Dict[str, List[str]]):
    length = 0
    queue = deque()
    queue.append(node)
    visit = set()

    while queue:
        for i in range(len(queue)):
            curr_node = queue.popleft()
            if curr_node == target:
                return length
            for neighbour in adjList[curr_node]:
                queue.append(neighbour)
                visit.add(neighbour)
        length += 1  # next layer
    return length


if __name__ == '__main__':
    # Given directed edges, build an adjacency list
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"], ["D", "C"]]

    adjList = {}

    for vertex_start, vertex_end in edges:
        if vertex_start not in adjList:
            adjList[vertex_start] = []
        if vertex_end not in adjList:
            adjList[vertex_end] = []
        adjList[vertex_start].append(vertex_end)
    print(adjList)
    print(bfs("A", "C", adjList))
