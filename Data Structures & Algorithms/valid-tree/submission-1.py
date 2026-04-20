class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # WANT TO CHECK
        # CONNECTED AND NO CYCLE EXISTS
        if len(edges) != n - 1:
            return False
 
        adjList = {i: [] for i in range(n)}

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        s = [0]
        visited = {0}

        while s:
            num = s.pop()
            for nei in adjList[num]:
                if nei in visited:
                    continue
                s.append(nei)
                visited.add(nei)
        return len(visited) == n
         

