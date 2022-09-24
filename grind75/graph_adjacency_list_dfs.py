# Count paths (backtracking)
def dfs(node: str, target: str, adjList, visit):
    # if the node is visited already exit
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbour in adjList[node]:
        count += dfs(neighbour, target, adjList, visit)
    visit.remove(node)
    return count


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
    print(dfs("A", "E", adjList, set()))
