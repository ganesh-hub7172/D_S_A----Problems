class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node): 
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            copy = Node(curr.val)
            visited[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
