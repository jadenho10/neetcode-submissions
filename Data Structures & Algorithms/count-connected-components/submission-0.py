class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]
        queue = deque()
        visit = set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def bfs(node):
            visit.add(node)
            queue.append(node)
            while queue:
                n = queue.popleft()
                for num in adjList[n]:
                    if num not in visit:
                        visit.add(num)
                        queue.append(num)
        
        count = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                count += 1

        return count
        