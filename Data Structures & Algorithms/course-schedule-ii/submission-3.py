class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            indegree[crs] += 1

        q = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                q.append(i)
        
        res, count = [], 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)
                count += 1
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        return res if count == numCourses else []