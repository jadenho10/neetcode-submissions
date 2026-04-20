class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(len(edges) + 1)]
        indegree = [0] * (len(edges) + 1)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                indegree[node] -= 1
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]