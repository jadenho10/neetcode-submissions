class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visit = set()

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def bfs(num):
            q = deque([num])

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in adjList[node]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
        
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                bfs(i)
        return count