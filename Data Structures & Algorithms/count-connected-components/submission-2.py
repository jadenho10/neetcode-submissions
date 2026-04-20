class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        def bfs(node):
            q = deque([node])
            visit.add(node)
            while q:
                curr = q.popleft()
                for nei in adjList[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        count = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                count += 1
        return count