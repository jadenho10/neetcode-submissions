class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            adjList[u].append([v, val])
            adjList[v].append([u, 1 / val])

        def bfs(src, tgt):
            if src not in adjList:
                return -1
            q = deque()
            q.append([src, 1])
            visit = set()
            while q:
                node, val = q.popleft()
                if node == tgt:
                    return val
                
                for nei, wei in adjList[node]:
                    if nei not in visit:
                        q.append([nei, val * wei])
                        visit.add(nei)
            return -1
        res = [0] * len(queries)
        for i in range(len(queries)):
            src, tgt = queries[i]
            res[i] = bfs(src, tgt)
        return res
