class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i, num in enumerate(indegree):
            if not num:
                q.append(i)

        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        q.append(nei)
            

        return res if len(res) == numCourses else []