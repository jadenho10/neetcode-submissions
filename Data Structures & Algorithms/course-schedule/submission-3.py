class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses + 1)]

        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            indegree[crs] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            crs = q.popleft()
            count += 1
            for preq in adjList[crs]:
                indegree[preq] -= 1
                if indegree[preq] == 0:
                    q.append(preq)
        return count == numCourses
