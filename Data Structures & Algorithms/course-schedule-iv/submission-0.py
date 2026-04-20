class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPreq = [set() for _ in range(numCourses)]
        for preq, crs in prerequisites:
            adjList[preq].add(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                isPreq[nei].add(node)
                isPreq[nei].update(isPreq[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return [u in isPreq[v] for u, v in queries]
        
        
