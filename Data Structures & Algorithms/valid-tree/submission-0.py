class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visit = set()
        def dfs(num, prev):
            if num in visit:
                return False
            visit.add(num)
            for j in adjList[num]:
                if prev == j:
                    continue
                if not dfs(j, num):
                    return False
                
            return True
        return dfs(0, -1) and n == len(visit)
