class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # WANT TO CHECK
        # CONNECTED AND NO CYCLE EXISTS
        if len(edges) > n - 1:
            return False
        
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()
        
        q = deque([(0, -1)])
        
        visit.add(0)

        while q:
            node, par = q.popleft()
            for nei in adjList[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                q.append((nei, node))
                visit.add(nei)
        return len(visit) == n 
