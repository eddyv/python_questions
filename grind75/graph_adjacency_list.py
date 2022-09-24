class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []


# or use a hashmap
adjList = {"A": [], "B": []}

if __name__ == '__main__':
    # Given directed edges, build an adjacency list
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

    adjList = {}

    for vertex_start, vertex_end in edges:
        if vertex_start not in adjList:
            adjList[vertex_start] = []
        if vertex_end not in adjList:
            adjList[vertex_end] = []
        adjList[vertex_start].append(vertex_end)
    print(adjList)
