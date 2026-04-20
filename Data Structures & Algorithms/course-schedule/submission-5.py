class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)] 
        indegree = [0] * numCourses

        for crs, preq in prerequisites:
            adjList[preq].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return count == numCourses