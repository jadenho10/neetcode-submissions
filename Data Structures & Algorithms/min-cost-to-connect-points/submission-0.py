from math import sqrt
from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {i : [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < len(points):
            wei, node = heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res += wei

            for dist, nei in adjList[node]:
                if nei not in visit:
                    heappush(minHeap, [dist, nei])
        return res
        