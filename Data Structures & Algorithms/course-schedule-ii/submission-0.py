class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i: [] for i in range(numCourses)}
        for crs, preqs in prerequisites:
            hashmap[crs].append(preqs)
        
        res = []

        visit, cycle = set(), set()
        def dfs(num):
            if num in cycle:
                return False
            if num in visit:
                return True

            cycle.add(num)
            for preqs in hashmap[num]:
                if not dfs(preqs):
                    return False
            cycle.remove(num)
            visit.add(num)
            res.append(num)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res